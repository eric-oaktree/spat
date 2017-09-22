from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^setup/$', views.setup, name='setup'),
    url(r'^importd/$', views.load_x, name='importd'),
    #homepage
    url(r'^$', views.dash, name='dash'),

]
