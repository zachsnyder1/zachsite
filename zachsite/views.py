from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import QuestionAndAnswer
from projects.models import Project

@require_http_methods(["GET"])
def index(request):
	"""
	Home page routes to Spiel page.
	"""
	questionAnswerList = QuestionAndAnswer.objects.all().order_by("id")
	projectList = Project.objects.all().filter(active=True).order_by("title")
	context = {
		'QAs': questionAnswerList,
		'projectList': projectList,
		'projectLen': str(len(projectList))
	}
	return render(request, 'zachsite/index.html', context)

def error404(request):
	"""
	Serve custom 404.html template.
	"""
	projectList = Project.objects.all().filter(active=True).order_by("title")
	context = {
		'projectList': projectList,
	}
	return render(request, 'zachsite/404.html', context)
