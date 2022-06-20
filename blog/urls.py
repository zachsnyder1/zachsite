from django.urls import include, re_path
from . import views

urlpatterns = [
        re_path(r'^$', views.blog_entries, name='blog_entries'),
        re_path(r'^(?P<entry_uuid>[0-9A-Fa-f-]+)/(?P<entry_slug>[0-9A-Za-z_-]+)/$',
            views.blog_detail,
            name='blog_detail'),
]
