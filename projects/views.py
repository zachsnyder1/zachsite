from django.http import Http404
from django.shortcuts import render, get_object_or_404
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
    curr_project = get_object_or_404(Project, id=project_id)
    # make sure id matches slug
    if curr_project.slug != project_slug:
        raise Http404
    else:
        pass

    projectList = Project.objects.all().filter(active=True).order_by("title")
    codeExampleList = curr_project.codeexample_set.all()
    context = {
            'projectList': projectList,
            'projectLen': str(len(projectList)),
            'curr_project': curr_project,
            'codeExampleList': codeExampleList,
            'readme_location': 'projects/' + curr_project.slug + '/readme.html',
            'subnav_location': 'projects/' + curr_project.slug + '/subnav.html'
    }
    return render(request, 'projects/project_about.html', context)


@require_http_methods(["GET"])
def project_docs(request, project_id, project_slug):
    """
    Project docs page.
    """
    curr_project = get_object_or_404(Project, id=project_id)
    # make sure id matches slug and project has docs
    if (curr_project.slug != project_slug) or (not curr_project.has_docs):
        raise Http404
    else:
        pass

    projectList = Project.objects.all().filter(active=True).order_by("title")
    context = {
            'projectList': projectList,
            'projectLen': str(len(projectList)),
            'curr_project': curr_project,
            'docs_location': 'projects/' + curr_project.slug + '/docs.html',
            'subnav_location': 'projects/' + curr_project.slug + '/subnav.html'
    }
    return render(request, 'projects/project_docs.html', context)
