# Create your views here.

from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic import ListView, DetailView, TemplateView

from .models import *


class ProjectDetail(DetailView):
    """
    ================
    Project Detail View
    ================

    Text Detail View extended from the Django Generic DetailView. The Queryset
    has been overridden to only display published articles.
    """

    model = Project
    template_name = "partials/project_detail.html"

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        resume_list = ResumeItem.objects.filter(hide=False).order_by("-start_date")
        project_list = Project.objects.filter(published=True)\
            .order_by('order')


        context['resume_list'] = resume_list
        context['project_list'] = project_list

        return context
