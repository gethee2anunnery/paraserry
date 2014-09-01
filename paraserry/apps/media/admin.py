from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ContribUserAdmin
from django.contrib.admin.widgets import AdminFileWidget

from django.utils.translation import ugettext_lazy as _

from django.contrib import messages

from .models import *

class ImageAdmin(admin.ModelAdmin):
   
    fieldsets = (
        ( 'Media', { 'fields': ( 
            ('admin_thumbnail','image',),
            'image_variants',
            'title',
            'credit',
            'caption',
             ) 
        } ),        
    )
    list_display = ( 'admin_thumbnail','title', 'caption', 'credit', )
    list_editable = ()
    list_display_links = ( 'title', 'caption', 'credit',)
    sortable_field_name = ('admin_thumbnail',)
    readonly_fields  = ('admin_thumbnail','image_variants')
    search_fields = ("title", "caption", "credit",)


    def admin_thumbnail(self, obj):
        if obj.image:
            try:
                return "<img src='%s' />"%(obj.admin_thumbnail.url)
            except:
                return "Error displaying image"
    admin_thumbnail.allow_tags = True

    def image_variants(self, obj):
        if obj.image:
            return '<a href="%s">Original Size (%spx x %spx)</a><br />\
            <a href="%s">500 (%spx x %spx)</a><br />\
            <a href="%s">250 (%spx x %spx)</a><br />\
            <a href="%s">100 (%spx x %spx)</a><br />'%(obj.image.url, obj.image.width, \
            obj.image.height, obj.image_500.url, obj.image_500.width, obj.image_500.height, \
            obj.image_250.url, obj.image_250.width, obj.image_250.height, \
            obj.image_100.url, obj.image_100.width, obj.image_100.height )

    image_variants.allow_tags = True

class DocumentAdmin(admin.ModelAdmin):

    autocomplete_lookup_fields = {
        'fk': ['image']
    }
    raw_id_fields = ('image',)
   
    fieldsets = (
        ( 'Media', { 'fields': ( 
            ('media_file',),
            ('admin_thumbnail','image',),
            'title',
            ) 
        } ),        
    )
    list_display = ( 'admin_thumbnail', 'title',  )
    list_display_links = ('admin_thumbnail', 'title', )
    readonly_fields  = ('admin_thumbnail',)
    search_fields = ("title",)

    def admin_thumbnail(self, obj):
        if obj.image:
            if obj.image.image:
                try:
                    return "<img src='%s' />"%(obj.image.admin_thumbnail.url)
                except:
                    return "Error displaying Image"
    admin_thumbnail.allow_tags = True


admin.site.register(Image, ImageAdmin)
admin.site.register(Document, DocumentAdmin)