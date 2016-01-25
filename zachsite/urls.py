from django.conf.urls import url
from . import views
from django.conf.urls.defaults import handler404

urlpatterns = [
	url(r'^$', views.index, name='index'),
]

handler404 = 'zachsite.views.error404'
