import json
from typing import Union, overload

from bs4 import BeautifulSoup
from typing_extensions import Literal

from soup2dict.transformer import transform


@overload
def convert(
    soup: BeautifulSoup,
    *,
    as_json: Literal[False],
) -> dict:
    """Return dict when as_json is false."""


@overload
def convert(
    soup: BeautifulSoup,
    *,
    as_json: Literal[True],
) -> str:
    """Return json string when as_json is True."""


@overload
def convert(
    soup: BeautifulSoup,
) -> dict:
    """When as_json is not specified return value is a dict."""


def convert(
    soup: BeautifulSoup,
    *,
    as_json: bool = False,
) -> Union[dict, str]:
    """Run soup to dict transformer and dumps to json if as_json is True."""
    if as_json:
        return json.dumps(transform(soup))

    return transform(soup)
