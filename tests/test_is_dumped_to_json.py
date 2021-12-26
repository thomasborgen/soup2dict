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
                    'navigablestring': ['test'],
                },
                {
                    '#text': 'test',
                    'navigablestring': ['test'],
                },
            ],
        },
    ],
}


def test_as_json_true_dumps_to_json():
    """Convert result should be json when as_json is true."""
    soup = BeautifulSoup(html_doc, 'html.parser')

    assert convert(soup, as_json=True) == json.dumps(expected_result)
