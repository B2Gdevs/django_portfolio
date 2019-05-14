"""
Phone app models and supporting models.

Author: Benjamin Garrard
Date: 5/12/2019
"""
from django.db import models


class PhoneApp(models.Model):
    """
    Object responsible for maintaining information on phone apps.

    Attributes
    ----------
    app_name: CharField
        The app name for the phone app.

    app_description: TextField
        The app description telling what the app is for.

    image: ImageField
        The image that is used to have the app to be recognized.

    android_app_file: FileField
        The android app file.  The APK.

    ios_app_file: FileField
        The ios app file.  The binary file to which I do not know the name.

    """

    app_name = models.CharField(max_length=120)
    app_description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    android_app_file = models.FileField(upload_to='android_apps/', null=True, blank=True)
    ios_app_file = models.FileField(upload_to='ios_apps/', null=True, blank=True)

    class Meta:
        """Configures the database table name."""
        db_table = "phone_app"
