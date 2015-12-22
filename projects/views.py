from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Project

@require_http_methods(["GET"])
def projects_home(request):
	"""
	Projects home page.
	"""
	projectList = Project.objects.all().filter(active=True).order_by("title")
	context = {
		'projectList': projectList,
		'projectLen': str(len(projectList))
	}
	return render(request, 'projects/projects_home.html', context)

@require_http_methods(["GET"])
def project_about(request, project_id, project_slug):
	"""
	Project 'about' page.
	"""
	projectList = Project.objects.all().filter(active=True).order_by("title")
	curr_project = projectList.get(id=project_id)
	context = {
		'projectList': projectList,
		'projectLen': str(len(projectList)),
		'curr_project': curr_project,
	}
	return render(request, 'projects/project_about.html', context)
	
@require_http_methods(["GET"])
def project_docs(request, project_id, project_slug):
	"""
	Project docs page.
	"""
	projectList = Project.objects.all().filter(active=True).order_by("title")
	curr_project = projectList.get(id=project_id)
	context = {
		'projectList': projectList,
		'projectLen': str(len(projectList)),
		'curr_project': curr_project,
	}
	return render(request, 'projects/project_docs.html', context)