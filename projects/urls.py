from django.urls import include, re_path
from . import views

urlpatterns = [
        # Web app includes:
        re_path(r'^geopost/', include('geopost.urls')),
        # Projects app urls:
        re_path(r'^$', views.projects_home, name='projects_home'),
        re_path(r'^(?P<project_id>[0-9]+)/(?P<project_slug>[0-9A-Za-z_-]+)/$',
            views.project_about,
            name='project_about'),
        re_path(r'^(?P<project_id>[0-9]+)/(?P<project_slug>[0-9A-Za-z_-]+)/docs/$',
            views.project_docs,
            name='project_docs')
]
