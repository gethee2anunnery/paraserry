import urllib, os
import time
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from django.core.files import File
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from imagekit import ImageSpec
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.admin import AdminThumbnail
from imagekit.processors import ResizeToFill, ResizeToFit

def image_title_file_name( instance, filename ):
    """Generate Document File Name"""

    file, extension = os.path.splitext( filename )
    use_title = instance.title if instance.title else file
    short_title = slugify(use_title[:50])
    
    filename        = "%s-%s%s" % ( short_title, str( time.time() )[0:10], extension )
    filename        = filename.lower()
    return '/'.join( [ 'media', 'image', filename ] )

def document_file_name( instance, filename ):
    """Generate Document File Name"""

    file, extension = os.path.splitext( filename )    
    use_title = instance.title if instance.title else file
    short_title = slugify(use_title[:50])
    
    filename        = "%s-%s%s" % ( short_title, str( time.time() )[0:10], extension )
    filename        = filename.lower()
    return '/'.join( [ 'media', 'document', filename ] )


class Image( models.Model ):

    image = models.ImageField(upload_to=image_title_file_name)
    

    image_500 = ImageSpecField(source='image',
                                      processors=[ResizeToFit(500, 500)],
                                      format='PNG',
                                      options={'quality': 100})

    image_250 = ImageSpecField(source='image',
                                      processors=[ResizeToFit(250, 250)],
                                      format='PNG',
                                      options={'quality': 100})

    image_100 = ImageSpecField(source='image',
                                      processors=[ResizeToFit(100, 100)],
                                      format='PNG',
                                      options={'quality': 100})

    image_500_square = ImageSpecField(source='image',
                                      processors=[ResizeToFill(500, 500)],
                                      format='PNG',
                                      options={'quality': 100})

    image_250_square = ImageSpecField(source='image',
                                      processors=[ResizeToFill(250, 250)],
                                      format='PNG',
                                      options={'quality': 100})

    image_100_square = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 100)],
                                      format='PNG',
                                      options={'quality': 100})

    title = models.CharField(_("title"), max_length=255, help_text="Title is required")
    credit = models.CharField(_("Credit"), max_length=255, blank=True)
    caption = models.TextField(_("Caption"), blank = True )


    # -- Variations
    admin_thumbnail = ImageSpecField( source='image', format='JPEG', 
        processors=[ResizeToFit(150, 150)], options={'quality': 90})

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains", "credit__icontains","caption__icontains",'admin_description__icontains')

    def __unicode__(self):
        if self.title:
            return ("%s")%(self.title)
        elif self.caption:
            return ("%s %s")%(self.caption, self.credit)
        else:
            return ("Image %s")%(self.pk)

        

class Document( models.Model ):

    title = models.CharField(_("title"), max_length=255, help_text="Title is required")
    media_file = models.FileField(upload_to=document_file_name, blank=True, help_text="Documents, i.e. PDFs or Word docs")
    
    image = models.ForeignKey('Image', null=True, blank=True)


    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains", 'admin_description__icontains')

    def __unicode__(self):
        if self.title:
            return ("%s")%(self.title)
        else:
            return ("Document %s")%(self.pk)

