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
    url(r'^add_contact/(?P<v_id>\d+)/$', views.add_contact, name='add_contact'),
    url(r'^edit_contact/(?P<v_id>\d+)/$', views.edit_contact, name='edit_contact'),
    url(r'^del-check/(?P<v_id>\d+)/$', views.del_check, name='del_check'),
    url(r'^ksdjfhksjdhf/(?P<v_id>\d+)/$', views.delete_vendor, name='delete_vendor'),
    url(r'^av/$', views.add_vendor, name='add_vendor'),
    url(r'^ev/(?P<v_id>\d+)/$', views.edit_vendor, name='edit_vendor'),
    url(r'^vd/(?P<v_id>\d+)/$', views.vendor_detail, name='vendor_detail'),
    url(r'^cd/(?P<c_id>\d+)/$', views.contact_detail, name='contact_detail'),
    url(r'^$', views.vendor_home, name='vendor_home'),
]
