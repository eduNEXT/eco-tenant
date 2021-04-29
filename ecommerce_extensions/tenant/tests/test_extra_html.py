"""
Tests for the extra html.
"""
from __future__ import absolute_import, unicode_literals

from django.test import TestCase
from path import Path
from testfixtures import LogCapture

from ecommerce_extensions.tenant.extra_html import common_attributes, process_html
from ecommerce_extensions.tenant.extra_options import error_message, validate_option_attributes


class TestsProcessExtraHtml(TestCase):
    """ Tests for extra html"""

    def test_returned_process_html(self):
        """
        Test process_html function returns a dictionary with all the valid html
        in the correct order.
        """
        path = Path("/test")
        tenantoptions = {
            "html": {
                ".*/test": [
                    {
                        "content": "<h1>Hola Mundo START!</h1>"
                    },
                    {
                        "location": "body_end",
                        "content": "<h1>Hola Mundo END!</h1>"
                    },
                ]
            }
        }
        test_html = {
            "body_start": "<h1>Hola Mundo START!</h1>",
            "body_end": "<h1>Hola Mundo END!</h1>"
        }

        html_returns = process_html(path, tenantoptions)

        self.assertEqual(test_html, html_returns)

    def test_returned_(self):
        """
        Test process_html function returns only the html that have a valid configuration.
        """
        path = Path("/test")
        tenantoptions = {
            "html": {
                ".*/test": [
                    {
                        "location": "bodyend",
                        "content": "<h1>Hola Mundo END!</h1>"
                    },
                ]
            }
        }

        html_returns = process_html(path, tenantoptions)

        self.assertEqual({}, html_returns)

    def test_returned_path_html(self):
        """
        Test process_html function returns only the html that match the current request path.
        """
        path = Path("/test")
        tenantoptions = {
            "html": {
                ".*/dashboard": [
                    {
                        "location": "bodyend",
                        "content": "<h1>Hola Mundo END!</h1>"
                    },
                ]
            }
        }

        html_returns = process_html(path, tenantoptions)

        self.assertEqual({}, html_returns)

    def test_validate_option_attributes_fails_silently(self):
        """
        Test validate_option_attributes function logs error when a html has a missing/incorrect attribute.
        """
        values = {
            "location": "bodyend",
            "content": "<h1>Hola Mundo END!</h1>"
        }
        log_message = "{prefix} {error_message}".format(prefix="HTML", error_message=error_message) % "location"

        with LogCapture() as log:
            validate_option_attributes(
                values,
                common_attributes,
                "HTML"
            )
            log.check(("ecommerce_extensions.tenant.extra_options",
                       "ERROR",
                       log_message))
