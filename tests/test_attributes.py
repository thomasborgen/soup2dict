from bs4 import BeautifulSoup

from soup2dict import convert


def test_attributes_are_at_prepended():
    """Test that attributes are picked up and prepended with @."""
    html_doc = """
    <main class="bob arne" abc="test" style="color: red;" />
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    main_element = convert(soup)['main'][0]
    assert main_element['@class'] == ['bob', 'arne']
    assert main_element['@abc'] == 'test'
    assert main_element['@style'] == 'color: red;'
