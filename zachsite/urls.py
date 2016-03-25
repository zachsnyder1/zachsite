from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^accounts/login/$', auth_views.login),
	url(
		r'^accounts/logout/$', 
		auth_views.logout, 
		{'template_name': 'registration/logout.html'}
	),
	url(r'^registration/password_change/$', auth_views.password_change),
	url(r'^registration/password_change/done/$', auth_views.password_change_done),
	url(
		r'^registration/password_reset/$', 
		auth_views.password_reset,
		{'template_name': 'registration/pass_reset_form.html'}
	),
	url(r'^registration/password_reset/done/$', auth_views.password_reset_done),
	url(r'^registration/reset/$', auth_views.password_reset_confirm),
	url(r'^registration/reset/done/$', auth_views.password_reset_complete),
	url(r'^accounts/signup/$', views.Signup.as_view(), name="signup")
]
