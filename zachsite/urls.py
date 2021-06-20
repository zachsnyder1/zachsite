"""
Routing for zachsite app.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from projects.models import Project
from . import views

project_list = Project.objects.all().filter(active=True).order_by("title")
extra_context = {
    'projectList': project_list,
    'projectLen': str(len(project_list))
}

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(),
        {
            'template_name': 'zachsite/login.html',
            'extra_context': extra_context
        },
        name="login"
    ),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(),
        {
            'template_name': 'zachsite/logout.html',
            'extra_context': extra_context
        },
        name="logout"
    ),
    path(
        'accounts/password_change/',
        auth_views.PasswordChangeView.as_view(),
        {
            'template_name': 'zachsite/pass_change_form.html',
            'extra_context': extra_context
        },
        name="password_change"
    ),
    path(
        'accounts/password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        {
            'template_name': 'zachsite/pass_change_done.html',
            'extra_context': extra_context
        },
        name="password_change_done"),
    path(
        'accounts/password_reset/',
        auth_views.PasswordResetView.as_view(),
        {
            'template_name': 'zachsite/pass_reset_form.html',
            'extra_context': extra_context
        },
        name="password_reset"
    ),
    path(
        'accounts/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        {
            'template_name': 'zachsite/pass_reset_done.html',
            'extra_context': extra_context
        },
        name="password_reset_done"
    ),
    path(
        'accounts/reset/',
        auth_views.PasswordResetConfirmView.as_view(),
        {
            'template_name': 'zachsite/pass_reset_confirm.html',
            'extra_context': extra_context
        },
        name="password_reset_confirm"
    ),
    path(
        'accounts/reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        {
            'template_name': 'zachsite/pass_change_done.html',
            'extra_context': extra_context
        },
        name="password_reset_complete"
    )
]
