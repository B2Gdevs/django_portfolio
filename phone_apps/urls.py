from django.urls import path
import phone_apps.views as phone_app_views

urlpatterns = [
    path('', phone_app_views.app_index, name='phone_apps'),
    # path('android_app/<int:app_id>', phone_app_views.android_download,
    #      name="android_download"),
    # path('ios_app/<int:app_id>', phone_app_views.ios_download,
    #      name="ios_download")
]