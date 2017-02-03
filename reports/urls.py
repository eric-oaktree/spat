from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^rehome/atcsvdump/$', views.at_csv_dump, name='at_csv_dump'),

    url(r'^rehome/$', views.home, name='home'),
]
