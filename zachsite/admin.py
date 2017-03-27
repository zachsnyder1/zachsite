"""
Admin for zachsite app.
"""
from django.contrib import admin
from .models import QuestionAndAnswer

admin.site.register(QuestionAndAnswer)
