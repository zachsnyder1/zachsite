from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Home.as_view(), name='geopost_home'),
	url(r'^create$', views.CreatePost.as_view(), name='geopost_create'),
	url(r'^edit/(?P<entry_uuid>[0-9A-Fa-f-]+)$', 
		views.EditPost.as_view(), 
		name='geopost_edit'),
	url(r'^photo/(?P<entry_uuid>[0-9A-Fa-f-]+)$',
		views.photo,
		name="geopost_photo")
]