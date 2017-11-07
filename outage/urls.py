from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^setup/$', views.setup, name='setup'),
    url(r'^importd/$', views.load_x, name='importd'),
    url(r'^out_det/(?P<o_id>\d+)/$', views.outage_detail, name='outage_detail'),
    url(r'^new-outage/$', views.new_outage, name='new_outage'),
    url(r'^e-out/(?P<o_id>\d+)/$', views.edit_outage, name='edit_outage'),
    url(r'^out_csv_dump/$', views.out_csv_dump, name='out_csv_dump'),
    #homepage
    url(r'^$', views.dash, name='dash'),

]
