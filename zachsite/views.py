from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import QuestionAndAnswer
from projects.models import Project
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import SignupForm

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
		form = SignupForm()
		projectList = Project.objects.all().filter(active=True).order_by("title")
		context = {
			'form': form,
			'projectList': projectList,
			'projectLen': str(len(projectList))
		}
		return render(request, 'zachsite/signup.html', context)
		
	def post(self, request):
		"""
		Add new user.
		"""
		data = {
			'username': request.POST.get('username', False),
			'email': request.POST.get('email', False),
			'password': request.POST.get('password', False)
		}
		form = SignupForm(data)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			User.objects.create_user(username, email=email, password=password)
			return HttpResponseRedirect(reverse('login'))
		else:
			projectList = Project.objects.all().filter(active=True).order_by("title")
			context = {
				'form': form,
				'projectList': projectList,
				'projectLen': str(len(projectList))
			}
			return render(request, 'zachsite/signup.html', context)
	