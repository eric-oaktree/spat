from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^setup/$', views.setup, name='setup'),
    url(r'^importd/$', views.load_x, name='importd'),
    url(r'^out_det/(?P<o_id>\d+)/$', views.outage_detail, name='outage_detail'),
    #homepage
    url(r'^$', views.dash, name='dash'),

]
