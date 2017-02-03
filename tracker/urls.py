from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^closed/$', views.closed, name='closed'),
    url(r'^reqs/$', views.reqs, name='reqs'),
    url(r'^t/(?P<track_id>\d+)/$', views.detail, name='detail'),
    url(r'^f/(?P<track_id>\d+)/$', views.detailf, name='detailf'),
    url(r'^et/(?P<track_id>\d+)/$', views.edittracker, name='edittracker'),
    url(r'^ef/(?P<fin_id>\d+)/$', views.editfinance, name='editfinance'),
    url(r'^ef/(?P<fin_id>\d+)/$', views.editfinance, name='editfinance'),
    url(r'^nf/(?P<track_id>\d+)/$', views.newfinance, name='newfinance'),
    url(r'^nt/$', views.newtracker, name='newtracker'),
    url(r'^dyrwtd/(?P<track_id>\d+)/$', views.chk_del, name='chk_del'),
    url(r'^fasdgalaksjdnfnfnf/(?P<track_id>\d+)/$', views.delete, name='delete'),
    #homepage
    url(r'^$', views.index, name='index'),

]
