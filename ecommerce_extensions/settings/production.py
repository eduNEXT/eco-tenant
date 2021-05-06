"""
Production Django settings for ecommerce_extensions project.
"""

from __future__ import unicode_literals

# Sentry sentry_sdk
try:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
except ImportError:
    sentry_sdk = DjangoIntegration = None


def plugin_settings(settings)
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    # Sentry Integration
    sentry_integration_dsn = getattr(settings, 'ENV_TOKENS', {}).get(
        'ECOMMERCE_EXTENSIONS_SENTRY_INTEGRATION_DSN',
        settings.ECOMMERCE_EXTENSIONS_SENTRY_INTEGRATION_DSN
    )

    if sentry_sdk is not None and sentry_integration_dsn is not None:
        sentry_sdk.init(
            dsn=sentry_integration_dsn,
            integrations=[
                DjangoIntegration(),
            ],
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=0.1,

            # If you wish to associate users to errors (assuming you are using
            # django.contrib.auth) you may enable sending PII data.
            send_default_pii=True,
        )
