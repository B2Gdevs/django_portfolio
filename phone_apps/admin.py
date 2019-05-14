"""
Registers the phone apps to the admin page.

Author: Benjamin Garrard
Date: 5/12/2019
"""
from django.contrib import admin
from .models import PhoneApp


class PhoneAppAdmin(admin.ModelAdmin):
    """Set the display name to the app name only."""

    list_display = ('app_name',)


admin.site.register(PhoneApp, PhoneAppAdmin)
