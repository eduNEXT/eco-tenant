"""
This function gets called during every request by the
context processor to return all the custom html for a specific path.
"""
import re

from ecommerce_extensions.tenant.extra_options import check_attribute, validate_option_attributes

common_attributes = {'location': {'options': ['head', 'body_start', 'body_end'], 'default': 1}}


def process_html(path, options):
    """
    Process and loads all the extra html for the template
    rendered during the request.

    Parameters:
        path (string): a regex for a url of a given site
        options (dict): a list of separate html separated by a path

    Returns:
        dict: a list of separate html scripts validated according to regex in path
    """
    html_list = options.get('html', {})
    html_returns = {}

    if not isinstance(html_list, dict):
        return html_returns

    for regex, values in html_list.items():
        regex_path_match = re.compile(regex)
        if regex_path_match.match(path):
            for html in values:
                validated_html = validate_option_attributes(
                    html,
                    common_attributes,
                    "HTML"
                )
                if validated_html:
                    validated_html_content = check_attribute(
                        html,
                        validated_html,
                        "content",
                        "HTML"
                    )
                    if validated_html_content:
                        html_returns[validated_html['location']] = validated_html['content']

    return html_returns
