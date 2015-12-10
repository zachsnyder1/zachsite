from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from projects.models import Project
from .models import Entry

@require_http_methods(["GET"])
def blog_entries(request):
	"""
	Blog main page.
	"""
	projectList = Project.objects.all().filter(active=True).order_by("title")
	entriesList = Entry.objects.all().order_by('-pub_date')[:5]
	context = {
		'projectList': projectList,
		'entriesList': entriesList,
	}
	return render(request, 'blog/blog_entries.html', context)

@require_http_methods(["GET"])
def blog_detail(request, entry_uuid, entry_slug):
	"""
	Individual blog entry.
	"""
	projectList = Project.objects.all().filter(active=True).order_by("title")
	entry = Entry.objects.get(uuid=entry_uuid)
	context = {
		'projectList': projectList,
		'entry': entry,
	}
	return render(request, 'blog/blog_detail.html', context)