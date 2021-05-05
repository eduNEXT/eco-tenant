"""
Production Django settings for ecommerce_extensions project.
"""

from __future__ import unicode_literals

try:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
except ImportError:
    sentry_sdk = DjangoIntegration = None

# Sentry Integration
    sentry_integration_dsn = "https://6b0a5c7f98b14a8bb3998aa4345ae9c4@o94678.ingest.sentry.io/5749202"

    if sentry_sdk is not None and sentry_integration_dsn is not None:
        sentry_sdk.init(
            dsn=sentry_integration_dsn,
            integrations=[
                DjangoIntegration(),
            ],
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production,
            traces_sample_rate=1.0,

            # If you wish to associate users to errors (assuming you are using
            # django.contrib.auth) you may enable sending PII data.
            send_default_pii=True
        )
