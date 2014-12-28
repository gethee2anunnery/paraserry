# Create your views here.

from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic import ListView, DetailView, TemplateView

from .models import *


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
