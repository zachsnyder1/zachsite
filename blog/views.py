from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from projects.models import Project
from .models import Entry


@require_http_methods(["GET"])
def blog_entries(request):
    """
    Blog main page.
    """
    projectList = Project.objects.all().filter(active=True).order_by("title")
    entriesList = Entry.objects.all().order_by('-pub_time')[:5]
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
    entry = get_object_or_404(Entry, uuid=entry_uuid)

    # make sure uuid and slug match
    if entry.slug != entry_slug:
        raise Http404
    else:
        pass

    projectList = Project.objects.all().filter(active=True).order_by("title")
    context = {
            'projectList': projectList,
            'entry': entry,
    }
    return render(request, 'blog/blog_detail.html', context)
