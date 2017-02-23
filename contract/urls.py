from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.recent_con, name='recent_con'),
]
