from bs4 import BeautifulSoup

from soup2dict import convert

html_doc = """
<html>
hei
<head>
    <title>The Dormouse's story</title>
    <title>bob</title>
</head>
<body>
    <p class="title">The <b>Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters;
    and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
"""


def test_conversion():
    """Create soup and convert it to dict."""
    soup = BeautifulSoup(html_doc, 'html.parser')

    dict_result = convert(soup)
    assert isinstance(dict_result, dict)
    assert len(dict_result)


def test_convert_search_result():
    """Test that we can convert a find_all search result."""
    soup = BeautifulSoup(html_doc, 'html.parser').find_all('a')
    dict_result = convert(soup)

    assert 'a' in dict_result
    assert len(dict_result['a']) == 3
