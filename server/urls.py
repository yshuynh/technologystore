"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from app.views import *
from server import settings

urlpatterns = [
    path('admin/logout/', LogoutAPI.as_view(), name="logout_api"),
    path('admin_login', AdminPageLoginAPI.as_view(), name="logout_api"),
    path('admin', RedirectView.as_view(url='admin/', permanent=False), name='admin2'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include('app.api_views.urls')),
    path('', MainPageAPI.as_view(), name='main_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + [url(r'.*', MainPageAPI.as_view(), name='main_page_catch_all')]
