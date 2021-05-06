"""
This function gets called during every request by the
extra_html and extra_scripts to validate all the custom html and scripts for a specific path.
"""
import logging

logger = logging.getLogger(__name__)

error_message = "could not get loaded. '%s' attribute is missing or is an invalid option."


def validate_option_attributes(values, common_attributes, error_message_prefix):
    """
    Validate common attributes for options extra.

    Parameters:
        values (dict): a option with values to validate according to common_attributes

    Returns:
        dict: a option with values validated according to common_attributes
    """
    option_attributes = {}

    for key, attr_values in common_attributes.items():

        value = values.get(key)

        try:
            if value is not None:
                attr_values['options'].index(value.lower())
                option_attributes[key] = value.lower()
            else:
                default = attr_values['default']
                option_attributes[key] = attr_values['options'][default]
        except (KeyError, ValueError):
            logger.error(
                "{prefix} {error_message}".format(prefix=error_message_prefix, error_message=error_message),
                key
            )

            return None

    return option_attributes


def check_attribute(values, option_attributes, attribute, error_message_prefix):
    """
    Validate the existence of an specific attribute.

    Parameters:
        values (dict): a option with values to validate according to common_attributes
        option_attributes (dict): a option with values validated according to common_attributes
        attribute (string): a key to search in the two parameters above

    Returns:
        dict: a option_attributes with new attribute added
    """
    try:
        option_attributes[attribute] = values[attribute]
    except KeyError:
        logger.error(
            "{prefix} {error_message}".format(prefix=error_message_prefix, error_message=error_message),
            attribute
        )

        return None

    return option_attributes
