"""TensorflowServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.generic import RedirectView
# from django.contrib import admin
from classify_image.views import classify, classify_api
from django.urls import path ,include,re_path
urlpatterns = [
    re_path(r'^classify_image/classify/api/$', classify_api),
    re_path(r'^classify_image/classify/$', classify),
    re_path(r'^$', RedirectView.as_view(url='classify_image/classify/'))
  #  path('admin/', admin.site.urls),
]
