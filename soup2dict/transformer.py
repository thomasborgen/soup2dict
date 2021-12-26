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
def transform(instance) -> dict:
    """Convert beautifulsoup to dict. This is a typeclass definition."""


@transform.instance(BeautifulSoup)  # type: ignore
def _transform_bs(instance: BeautifulSoup) -> dict:
    """Handle The Soup."""
    return transform(instance.contents)


@transform.instance(element.ResultSet)  # type: ignore
@transform.instance(list)
def _transform_rs(instance: Union[element.ResultSet, list]) -> dict:
    """Handle list and ResultSet types."""
    transformed: Dict[str, Any] = {}

    for soup_element in instance:
        parsed = transform(soup_element)
        if not parsed:
            continue

        key_name = _get_key_name(soup_element)

        dict_value = transformed.get(key_name, [])
        dict_value.append(parsed)
        transformed[key_name] = dict_value

    return transformed


@transform.instance(element.NavigableString)  # type: ignore
@transform.instance(element.Comment)
@transform.instance(element.CData)
@transform.instance(element.ProcessingInstruction)
@transform.instance(element.XMLProcessingInstruction)
@transform.instance(element.Declaration)
@transform.instance(element.Doctype)
@transform.instance(element.Stylesheet)
@transform.instance(element.Script)
@transform.instance(element.TemplateString)
def _transform_ns(
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


@transform.instance(element.Tag)  # type: ignore
def _transform_tag(instance: element.Tag) -> dict:
    """Handle Tag type."""
    tag_result = _attribute_at_prepender(instance.attrs)
    tag_result['#text'] = ' '.join(
        [text.replace('\n    ', ' ') for text in instance.stripped_strings],
    )
    tag_result.update(transform(instance.contents))

    return tag_result
