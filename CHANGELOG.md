# Version history

| Change | Bumps |
| - | - |
| Breaking | major |
| New Feature | minor |
| otherwise | patch |


## Latest changes

## 2.0.0

No new features in this release, but we now support python 3.9 and 3.10


### Breaking

* soup2dict drops python 3.6 support

### Features

* Add support for python 3.9 and 3.10

### Internal

* Fixes poetry install in github workflows
* Cleans up github workflow
* Add python 3.9 and 3.10 to github workflows


## 1.0.1 - The License

Patch adds MIT LICENSE and updates metadata in pyproject.toml


## 1.0.0 - The Converter

First Release. Should be able handle most BeautifulSoup stuff

### Features

* BeautifulSoup to dictionary converter
* Converts BeautifulSoup, ResultSet, (list), Tag and all descendants of NavigableString Classes.
* tag attributes are prefixed with `@`
* text data is contained in `#text` key
* `@class` is always a list of 1-many classes if it exists on the element
* all sub elements are `element_name` keys with an array containing 1 to many dictionaries.
