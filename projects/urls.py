from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.projects_home, name='projects_home'),
	url(r'^(?P<project_id>[0-9]+)/(?P<project_slug>[0-9A-Za-z_-]+)/$', 
		views.project_about, 
		name='project_about'),
	url(r'^(?P<project_id>[0-9]+)/(?P<project_slug>[0-9A-Za-z_-]+)/docs/$',
		views.project_docs,
		name='project_docs')
]
