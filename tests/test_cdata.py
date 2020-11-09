from bs4 import BeautifulSoup

from soup2json import convert


def test_cdata_stringified():
    """Create soup and check elements are arrays."""
    html_doc = """
    <main>
        <![CDATA[A CDATA block]]>
    </main>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    main = convert(soup)['main'][0]
    assert main['cdata'] == ['A CDATA block']
