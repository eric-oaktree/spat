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
    url(r'^add-po/$', views.add_po, name='add_po'),
    url(r'^edit-po/(?P<po_id>\d+)/$', views.edit_po, name='edit_po'),
    url(r'^al/(?P<po_id>\d+)/$', views.add_line, name='add_line'),
    url(r'^el/(?P<ln_id>\d+)/$', views.edit_line, name='edit_line'),
    url(r'^(?P<po_id>\d+)/$', views.po_detail, name='po_detail'),
    url(r'^by-vendor/(?P<v_id>\d+)/$', views.po_by_vendor, name='po_by_vendor'),
    url(r'^add-to-vendor/(?P<v_id>\d+)/$', views.add_po_to_vendor, name='add_po_to_vendor'),
    url(r'^$', views.po_home, name='po_home'),
]
