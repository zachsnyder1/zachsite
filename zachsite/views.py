from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import QuestionAndAnswer
from projects.models import Project
from django.views.generic import View

@require_http_methods(["GET"])
def index(request):
	"""
	Zach-Site home page.
	"""
	questionAnswerList = QuestionAndAnswer.objects.all().order_by("id")
	projectList = Project.objects.all().filter(active=True).order_by("title")
	context = {
		'QAs': questionAnswerList,
		'projectList': projectList,
		'projectLen': str(len(projectList))
	}
	return render(request, 'zachsite/index.html', context)

class Signup(View):
	"""
	View class for signup page.
	"""
	def get(self, request):
		"""
		Render signup page.
		"""
		projectList = Project.objects.all().filter(active=True).order_by("title")
		context = {
			'projectList': projectList,
			'projectLen': str(len(projectList))
		}
		return render(request, 'zachsite/signup.html', context)
		
	def post(self, request):
		"""
		Add new user.
		"""
		pass
	