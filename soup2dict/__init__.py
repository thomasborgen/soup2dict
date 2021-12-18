import json
from typing import TYPE_CHECKING, Literal, Union, overload

from soup2dict.transformer import transform

if TYPE_CHECKING:
    from bs4 import BeautifulSoup


@overload
def convert(
    soup: 'BeautifulSoup',
    as_json: Literal[False],
) -> dict:
    """Return dict when as_json is false."""


@overload
def convert(
    soup: 'BeautifulSoup',
    as_json: Literal[True],
) -> str:
    """Return json string when as_json is True."""


def convert(
    soup: 'BeautifulSoup',
    as_json: bool = False,
) -> Union[dict, str]:
    """Run soup to dict transformer and dumps to json if as_json is True."""
    if as_json:
        return json.dumps(transform(soup))

    return transform(soup)
