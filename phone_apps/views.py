import os
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, Http404
from .models import PhoneApp


def app_index(request):
    """
    app_index gives a list of the phone apps that are on the web app.

    This method lists the phone apps in a column and allows them to be
    downloaded.

    Parameters
    ----------
    request : Request
        Request is the request made to the web server such as POST, GET, and
        etc.

    Returns
    -------
    render : render
        Render is the object that renders the html, injects the data, and
        displays everything to the user
    """
    apps = PhoneApp.objects.all()

    context = {'apps': apps}

    return render(request, 'app_index.html', context)


# def android_download(request, app_id):
#     obj = get_object_or_404()
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.android.package-archive")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404


# def ios_download(request, app_id):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/octet-stream ipa")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404