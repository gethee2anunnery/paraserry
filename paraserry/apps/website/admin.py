from django.contrib import admin

from .models import Project, Tag

class ProjectAdmin( admin.ModelAdmin ):
    """
    Option Admin Configuration
    """
    fieldsets = (
        ( 'Project', { 'fields': ( 'project_title', 'txtid', 'launch_date', 'main_url', 'about', 'tags' ) } ),
    )
    raw_id_fields = ('tags',)
    autocomplete_lookup_fields = {
        'fk': [],
        'm2m': [ 'tags' ],
    }
    list_display    = [ 'project_title', ]
    prepopulated_fields = {'txtid': ('project_title',)}


class TagAdmin(admin.ModelAdmin):
    """
    Admin configuration for Tags
    """

    fieldsets = (
        ( 'Tag', { 'fields': ( 'parent', ('title', 'slug'), 'published' ) } ),

    )
    raw_id_fields = ('parent',)
    autocomplete_lookup_fields = {
        'fk': ['parent'],
        'm2m': [ ],
    }
    list_display = ('slug', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register( Project, ProjectAdmin )
admin.site.register( Tag, TagAdmin )