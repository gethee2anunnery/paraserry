from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView, RedirectView


from paraserry.apps.website.views import *

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/',  include(admin.site.urls)), # admin site

    url(r'^projects/(?P<pk>[\w-]+)/$', ProjectDetail.as_view(), name='project'),
    url(r'^projects/$', ProjectList.as_view(), name = 'projects'),

    url(r'^$', ResumeList.as_view(template_name='home.html'), name="home"),
)
