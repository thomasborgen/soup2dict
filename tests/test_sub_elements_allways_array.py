from bs4 import BeautifulSoup

from soup2dict import convert

html_doc = """
<main>
</main>
<main>
    <sub>test</sub>
    <sub>test</sub>
    <sub>test</sub>
</main>
"""


def test_sub_elements_allways_array():
    """Create soup and check elements are arrays."""
    soup = BeautifulSoup(html_doc, 'html.parser')

    dict_result = convert(soup)

    assert len(dict_result['main']) == 2
    assert len(dict_result['main'][1]['sub']) == 3
