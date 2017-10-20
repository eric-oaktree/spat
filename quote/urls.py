"""collywop URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^q/(?P<q_id>\d+)/$', views.quotes_detail, name='quotes_detail'),
    url(r'^p/(?P<p_id>\d+)/$', views.project_detail, name='project_detail'),
    url(r'^p/$', views.project_home, name='project'),
    url(r'^$', views.quotes_home, name='quotes_home'),

]
