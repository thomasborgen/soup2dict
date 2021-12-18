import json

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

expected_result = {
    'main': [
        {'#text': ''},
        {
            '#text': 'test test test',
            'sub': [
                {
                    '#text': 'test',
                    'navigablestring': ['test'],
                },
                {
                    '#text': 'test',
                    'navigablestring': ['test']
                },
                {
                    '#text': 'test',
                    'navigablestring': ['test'],
                },
            ],
        },
    ],
}


def test_sub_elements_allways_array():
    """Create soup and check elements are arrays."""
    soup = BeautifulSoup(html_doc, 'html.parser')

    assert convert(soup, as_json=True) == json.dumps(expected_result)
