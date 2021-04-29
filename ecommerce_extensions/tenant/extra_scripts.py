"""
This function gets called during every request by the
context processor to return all the custom scripts for a specific path.
"""
import re

from ecommerce_extensions.tenant.extra_options import check_attribute, validate_option_attributes

common_attributes = {'type': {'options': ['inline', 'external']},
                     'media_type': {'options': ['module', 'text/javascript'], 'default': 1}}


def process_scripts(path, options):
    """
    Process and loads all the extra scripts for the template
    rendered during the request.

    Parameters:
        path (string): a regex for a url of a given site
        options (dict): a list of javascript scripts separated by a path

    Returns:
        dict: a list of separate javascript scripts validated according to regex in path
    """
    scripts = options.get('scripts', {})

    if isinstance(scripts, dict):
        for regex, values in scripts.items():
            regex_path_match = re.compile(regex)
            if regex_path_match.match(path):
                scripts = []
                for script in values:
                    validated_script = validate_option_attributes(
                        script,
                        common_attributes,
                        "Script"
                    )

                    if validated_script:
                        # Validate according to the script type
                        attr = 'content' if validated_script['type'] == 'inline' else 'src'
                        validated_script = check_attribute(
                            script,
                            validated_script,
                            attr,
                            "Script"
                        )
                        scripts.append(validated_script)
                if scripts:
                    return scripts

    return None
