from django.contrib import admin

from .models import Project

class ProjectAdmin( admin.ModelAdmin ):
    """
    Option Admin Configuration
    """
    fieldsets = (
        ( 'Project', { 'fields': ( 'project_title', 'txtid', 'launch_date', 'main_url', 'about' ) } ),
    )
    list_display    = [ 'project_title', ]
    prepopulated_fields = {'txtid': ('project_title',)}


admin.site.register( Project, ProjectAdmin )