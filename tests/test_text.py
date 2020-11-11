from bs4 import BeautifulSoup

from soup2dict import convert


def test_direct_descendants_text_are_caught():
    """Create soup and check elements are arrays."""
    html_doc = """
    <main>
        Hello
        <b>can you hear me</b>
        <div><div>test</div></div>
        Hello
    </main>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    main = convert(soup)['main'][0]

    assert main['#text'] == 'Hello can you hear me test Hello'
    assert main['b'][0]['#text'] == 'can you hear me'
