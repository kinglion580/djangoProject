"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.views import serve
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)


urlpatterns = [
    path('Yeling/djangoProject/', views.index, name='index'),
    path('Yeling/djangoProject/execute/', views.execute, name='execute'),
    path('Yeling/djangoProject/get_message/', views.get_message, name='get_message'),
    path('admin/', admin.site.urls),
    path('progressbar/', include('progress_bar.urls')),
    path('Yeling/djangoProject/realtime/', include('realtime.urls')),
    re_path(r'Yeling/djangoProject/static/(?P<path>.*)$', return_static, name='static'),
]