"""
Tests for the extra scripts.
"""
from __future__ import absolute_import, unicode_literals

from django.test import TestCase
from path import Path
from testfixtures import LogCapture

from ecommerce_extensions.tenant.extra_options import error_message, validate_option_attributes
from ecommerce_extensions.tenant.extra_scripts import common_attributes, process_scripts


class TestsProcessExtraScripts(TestCase):
    """ Tests for extra scripts"""

    def test_returned_process_scripts(self):
        """
        Test process_scripts function returns a dictionary with all the valid scripts
        in the correct order.
        """
        path = Path("/test")
        tenantoptions = {
            "scripts": {
                ".*/test": [
                    {
                        "src": "https://www.test-external-script.com/js/myScript1.js",
                        "type": "external",
                        "media_type": "module"
                    },
                    {
                        "content": "alert('This alert box was called with the onload event');",
                        "type": "inline"
                    }
                ]
            }
        }
        test_scripts = [
            {
                "src": "https://www.test-external-script.com/js/myScript1.js",
                "type": "external",
                "media_type": "module"
            },
            {
                "content": "alert('This alert box was called with the onload event');",
                "type": "inline",
                "media_type": "text/javascript"
            },
        ]

        scripts = process_scripts(path, tenantoptions)

        self.assertEqual(test_scripts, scripts)

    def test_returned_(self):
        """
        Test process_scripts function returns only the scripts that have a valid configuration.
        """
        path = Path("/test")
        tenantoptions = {
            "scripts": {
                ".*/test": [
                    {
                        "content": "alert('This alert box was called with the onload event');",
                        "type": "src"
                    }
                ]
            }
        }

        scripts = process_scripts(path, tenantoptions)

        self.assertIsNone(scripts)

    def test_returned_path_scripts(self):
        """
        Test process_scripts function returns only the scripts that match the current request path.
        """
        path = Path("/test")
        tenantoptions = {
            "scripts": {
                ".*/dashboard": [
                    {
                        "src": "https://www.test-external-script.com/js/myScript1.js",
                        "type": "external",
                        "media_type": "text/javascript"
                    }
                ]
            }
        }

        scripts = process_scripts(path, tenantoptions)

        self.assertIsNone(scripts)

    def test_validate_option_attributes_fails_silently(self):
        """
        Test validate_option_attributes function logs error when a script has a missing/incorrect attribute.
        """
        values = {
            "tpe": "external",
            "media_type": "text/javascript"
        }
        log_message = "{prefix} {error_message}".format(prefix="Script", error_message=error_message) % "type"

        with LogCapture() as log:
            validate_option_attributes(
                values,
                common_attributes,
                "Script"
            )
            log.check(("ecommerce_extensions.tenant.extra_options",
                       "ERROR",
                       log_message))
