# Create your views here.

from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic import ListView, DetailView

from .models import Project


class ProjectList(ListView):
    """
    ==============
    Project List View
    ==============

    Project list view that extends the Django Generic Views List View. 
    """
    model = Project
    template_name = "projects/project_list.html"

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset


class ProjectDetail(DetailView):
    """
    ================
    Project Detail View
    ================

    Text Detail View extended from the Django Generic DetailView. The Queryset
    has been overridden to only display published articles.
    """

    model = Project
    template_name = "projects/project_detail.html"

