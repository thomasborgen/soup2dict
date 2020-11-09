# Soup2Json

BeautifulSoup4 to python dictionary and json converter
___
![test](https://github.com/thomasborgen/beautifuldict/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/thomasborgen/beautifuldict/branch/master/graph/badge.svg)](https://codecov.io/gh/thomasborgen/beautifuldict)
[![Python Version](https://img.shields.io/pypi/pyversions/beautifuldict.svg)](https://pypi.org/project/beautifuldict/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
___

## Installation

Get package with pip or poetry

```sh
pip install soup2json
```

```sh
poetry add soup2json
```

## Example

```python

from bs4 import BeautifulSoup

from soup2json import convert

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


# Create soup from html_doc data
soup = BeautifulSoup(html_doc, 'html.parser')

# Convert it to a dictionary with convert()
dict_result = convert(soup)

print(dict_result)
```

## Output

```json
{
  "html": [
    {
      "#text": "hei The Dormouse's story bob The Dormouse's story Once upon a time there were three little sisters; and their names were Elsie , Lacie and Tillie ; and they lived at the bottom of a well. ...",
      "navigablestring": [
        "hei"
      ],
      "head": [
        {
          "#text": "The Dormouse's story bob",
          "title": [
            {
              "#text": "The Dormouse's story",
              "navigablestring": [
                "The Dormouse's story"
              ]
            },
            {
              "#text": "bob",
              "navigablestring": [
                "bob"
              ]
            }
          ]
        }
      ],
      "body": [
        {
          "#text": "The Dormouse's story Once upon a time there were three little sisters; and their names were Elsie , Lacie and Tillie ; and they lived at the bottom of a well. ...",
          "p": [
            {
              "@class": [
                "title"
              ],
              "#text": "The Dormouse's story",
              "navigablestring": [
                "The"
              ],
              "b": [
                {
                  "#text": "Dormouse's story",
                  "navigablestring": [
                    "Dormouse's story"
                  ]
                }
              ]
            },
            {
              "@class": [
                "story"
              ],
              "#text": "Once upon a time there were three little sisters; and their names were Elsie , Lacie and Tillie ; and they lived at the bottom of a well.",
              "navigablestring": [
                "Once upon a time there were three little sisters;\n    and their names were",
                ",",
                "and",
                ";\n    and they lived at the bottom of a well."
              ],
              "a": [
                {
                  "@href": "http://example.com/elsie",
                  "@class": [
                    "sister"
                  ],
                  "@id": "link1",
                  "#text": "Elsie",
                  "navigablestring": [
                    "Elsie"
                  ]
                },
                {
                  "@href": "http://example.com/lacie",
                  "@class": [
                    "sister"
                  ],
                  "@id": "link2",
                  "#text": "Lacie",
                  "navigablestring": [
                    "Lacie"
                  ]
                },
                {
                  "@href": "http://example.com/tillie",
                  "@class": [
                    "sister"
                  ],
                  "@id": "link3",
                  "#text": "Tillie",
                  "navigablestring": [
                    "Tillie"
                  ]
                }
              ]
            },
            {
              "@class": [
                "story"
              ],
              "#text": "...",
              "navigablestring": [
                "..."
              ]
            }
          ]
        }
      ]
    }
  ]
}
```
