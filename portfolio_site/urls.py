"""portfolio_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import portfolio_site.views as general_views
from project.views import detail as project_detail
from predictions.views import nba_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', general_views.home, name='home'),
    path('', general_views.home, name='home'),
    path('project/<int:project_id>', project_detail, name='project_detail'),
    # path('contact/', general_views.contact, name='contact')
    path('contact/', general_views.home, name='contact'),
    path('predictions/nba', nba_view, name='nba_predictions'),
    path('algorithms', include('algorithms.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
