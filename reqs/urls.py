from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cda/$', views.cda_req, name='cda_req'),
    url(r'^gartner/$', views.gartner_req, name='gartner_req'),
    url(r'^all/$', views.reqs, name='reqs'),
]
