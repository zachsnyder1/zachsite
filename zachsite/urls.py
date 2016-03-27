from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(
		r'^accounts/login/$', 
		auth_views.login, 
		{'template_name': 'zachsite/login.html'},
		name="login"
	),
	url(
		r'^accounts/logout/$', 
		auth_views.logout,
		{'template_name': 'zachsite/logout.html'},
		name="logout"
	),
	url(
		r'^accounts/password_change/$', 
		auth_views.password_change,
		{'template_name': 'zachsite/pass_change_form.html'},
		name="password_change"
	),
	url(
		r'^accounts/password_change/done/$', 
		auth_views.password_change_done,
		{'template_name': 'zachsite/pass_change_done.html'},
		name="password_change_done"),
	url(
		r'^accounts/password_reset/$', 
		auth_views.password_reset,
		{'template_name': 'zachsite/pass_reset_form.html'},
		name="password_reset"
	),
	url(
		r'^accounts/password_reset/done/$', 
		auth_views.password_reset_done,
		{'template_name': 'zachsite/pass_reset_done.html'},
		name="password_reset_done"
	),
	url(
		r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
		auth_views.password_reset_confirm,
		{'template_name': 'zachsite/pass_reset_confirm.html'},
		name="password_reset_confirm"
	),
	url(
		r'^accounts/reset/done/$', 
		auth_views.password_reset_complete,
		{'template_name': 'zachsite/pass_change_done.html'},
		name="password_reset_complete"
	),
	url(r'^accounts/signup/$', views.Signup.as_view(), name="signup")
]
