"""
Views for zachsite app.
"""

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from projects.models import Project
from .models import QuestionAndAnswer


@require_http_methods(["GET"])
def index(request):
    """
    Zach-Site home page.
    """
    question_answer_list = QuestionAndAnswer.objects.all().order_by("id")
    project_list = Project.objects.all().filter(active=True).order_by("title")
    context = {
        'QAs': question_answer_list,
        'projectList': project_list,
        'projectLen': str(len(project_list))
    }
    return render(request, 'zachsite/index.html', context)
