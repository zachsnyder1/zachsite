from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.blog_entries, name='blog_entries'),
        url(r'^(?P<entry_uuid>[0-9A-Fa-f-]+)/(?P<entry_slug>[0-9A-Za-z_-]+)/$',
            views.blog_detail,
            name='blog_detail'),
]
