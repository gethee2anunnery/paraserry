from django.contrib import admin

from .models import *


class ResumeDetailInline(admin.StackedInline):
    fields = ( 
        'order', 'description', ('hide',)
    )
    model                   = ResumeItemDetail
    extra                   = 0
    list_display            = ['order' ]
    order_by                = 'order'


class ContentBlockInline(admin.StackedInline):
    fields = ( 
        'order','content', ('images','documents',)
    )
    model                   = ContentBlock
    extra                   = 0
    list_display            = [ ]
    raw_id_fields = ('images','documents')
    autocomplete_lookup_fields = {
        'fk': ['images','documents'],
        'm2m': [ ],
    }


class ProjectAdmin( admin.ModelAdmin ):
    """
    Option Admin Configuration
    """
    def admin_thumbnail(self, obj):
        if obj.feature_image:
            try:
                return "<img src='%s' />"%(obj.feature_image.admin_thumbnail.url)
            except:
                return "Error displaying image"
    admin_thumbnail.allow_tags = True
    fieldsets = (
        ( 'Project', { 'fields': ( 
            ('project_title', 'order'),
            ('txtid', 'published' ),
            ('feature_image', 'admin_thumbnail'),

            ('client', 'launch_date'), 
            'main_url', 'about', 'tags' ) } ),
    )
    raw_id_fields = ('tags', 'feature_image')
    autocomplete_lookup_fields = {
        'fk': ['feature_image'],
        'm2m': [ 'tags' ],
    }
    list_display    = [ 'project_title', 'client', 'published', 'order', 'admin_thumbnail' ]
    prepopulated_fields = {'txtid': ('project_title',)}
    readonly_fields = ('admin_thumbnail',)
    inlines             = [ContentBlockInline]
    list_editable = ('published', 'order',)
    order_by = ('order', 'project_title')


class LinkItemAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ( 'Link Items', { 'fields': ('parent','display_name',  'txtid', 'order',
            ('hide'), 
            'url', ) } ),
    )
    
    list_display = ('admin_title', 'display_name', 'hide',)
    list_display_links = ('display_name',)
    list_filter = ('parent',)
    readonly_fields = ('txtid',)
    autocomplete_lookup_fields = {
        'fk': ['parent']
    }
    raw_id_fields = ('parent',)
    actions = ('reindex_items',)
    ordering = ('path',)


    def lookup_allowed(self, key, value):
        """Enable Admin Filtering by Parent TextID"""
        if key in ('parent__txtid',):
            return True

        return super(LinkItemAdmin, self).lookup_allowed(key, value)


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


class ResumeItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for CV
    """

    fieldsets = (
        ( 'CV', { 'fields': ( ('title', 'hide'), 'employer', ('start_date', 'end_date'), 'description' ) } ),

    )

    list_display = ('title', 'employer')
    inlines = [ ResumeDetailInline ]



admin.site.register( Project, ProjectAdmin )
admin.site.register(LinkItem, LinkItemAdmin)
admin.site.register( ResumeItem, ResumeItemAdmin )
admin.site.register( Tag, TagAdmin )