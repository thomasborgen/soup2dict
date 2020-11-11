from bs4 import BeautifulSoup

from soup2dict import convert


def test_template_contains_templatestring():
    """Template element contains templatestring array."""
    html_doc = """
    <main>
        <template>test</template>
    </main>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    main = convert(soup)['main'][0]
    assert main['template'][0]['templatestring'] == ['test']
