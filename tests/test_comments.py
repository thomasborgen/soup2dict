from bs4 import BeautifulSoup

from soup2dict import convert


def test_tag_name_are_arrays():
    """Create soup and check elements are arrays."""
    html_doc = """
    <main>
        <!-- Html comment -->
    </main>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    dict_result = convert(soup)
    assert dict_result['main'][0]['comment'] == ['Html comment']
