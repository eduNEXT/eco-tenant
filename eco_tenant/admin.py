"""
Django admin page for custom eduNEXT models
"""
from django.contrib import admin

from eco_tenant.models import TenantOptions


class TenantOptionsAdmin(admin.ModelAdmin):
    """
    Admin interface for the TenantOptions object.
    """
    list_display = ('site', 'options_blob')
    search_fields = ('site__domain', 'options_blob')

    class Meta(object):
        """
        Meta class for TenantOptions admin model
        """
        model = TenantOptions


admin.site.register(TenantOptions, TenantOptionsAdmin)
