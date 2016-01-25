from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]

handler404 = 'zachsite.views.error404'
