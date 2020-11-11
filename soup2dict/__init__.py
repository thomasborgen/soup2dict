from typing import Any, Dict, Optional, Union

from bs4 import BeautifulSoup, element
from classes import typeclass


def _get_key_name(
    instance: Any,
):
    instance_type = type(instance)

    if instance_type == element.Tag:
        return instance.name

    return str(instance_type.__name__).lower()


def _attribute_at_prepender(
    instance: dict,
) -> dict:
    prefixed = {}
    for key, attribute_value in instance.items():
        prefixed['@{key}'.format(key=key)] = attribute_value
    return prefixed


@typeclass
def convert(instance) -> dict:
    """Convert beautifulsoup to dict. This is a typeclass definition."""


@convert.instance(BeautifulSoup)
def _convert_bs(instance: BeautifulSoup) -> dict:
    """Handle The Soup."""
    return convert(instance.contents)


@convert.instance(element.ResultSet)
@convert.instance(list)
def _convert_rs(instance: Union[element.ResultSet, list]) -> dict:
    """Handle list and ResultSet types."""
    transformed: Dict[str, Any] = {}

    for soup_element in instance:
        parsed = convert(soup_element)
        if not parsed:
            continue

        key_name = _get_key_name(soup_element)

        dict_value = transformed.get(key_name, [])
        dict_value.append(parsed)
        transformed[key_name] = dict_value

    return transformed


@convert.instance(element.NavigableString)  # type: ignore
@convert.instance(element.Comment)
@convert.instance(element.CData)
@convert.instance(element.ProcessingInstruction)
@convert.instance(element.XMLProcessingInstruction)
@convert.instance(element.Declaration)
@convert.instance(element.Doctype)
@convert.instance(element.Stylesheet)
@convert.instance(element.Script)
@convert.instance(element.TemplateString)
def _convert_ns(
    instance: Union[
        element.NavigableString,
        element.Comment,
        element.CData,
        element.ProcessingInstruction,
        element.XMLProcessingInstruction,
        element.Declaration,
        element.Doctype,
        element.Stylesheet,
        element.Script,
        element.TemplateString,
    ],
) -> Optional[str]:
    """Handle NavigableString type."""
    return str(instance).strip().strip('\n') or None


@convert.instance(element.Tag)
def _convert_tag(instance: element.Tag) -> dict:
    """Handle Tag type."""
    tag_result = _attribute_at_prepender(instance.attrs)
    tag_result['#text'] = ' '.join(
        [text.replace('\n    ', ' ') for text in instance.stripped_strings],
    )
    tag_result.update(convert(instance.contents))

    return tag_result
