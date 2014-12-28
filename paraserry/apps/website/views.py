# Create your views here.

from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic import ListView, DetailView

from .models import *


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
        queryset = Project.objects.filter(published=True)\
            .order_by('order')
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



class ResumeList(ListView):
    """
    ==============
    Project List View
    ==============

    Project list view that extends the Django Generic Views List View. 
    """
    model = ResumeItem
    #template_name = "home.html"

    def get_queryset(self):
        queryset = ResumeItem.objects.filter(hide=False).order_by("-start_date")
        return queryset