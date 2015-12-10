from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import QuestionAndAnswer, Blurb
from projects.models import Project

@require_http_methods(["GET"])
def index(request):
	"""
	Home page routes to Spiel page.
	"""
	questionAnswerList = QuestionAndAnswer.objects.all().order_by("id")
	projectList = Project.objects.all().filter(active=True).order_by("title")
	blurbList = Blurb.objects.all().order_by("id")
	context = {
		'QAs': questionAnswerList,
		'projectList': projectList,
		'projectLen': str(len(projectList)),
		'blurbList': blurbList,
		'blurbLen': str(len(blurbList))
	}
	return render(request, 'zachsite/index.html', context)