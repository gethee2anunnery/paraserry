from django.db import models
from datetime import datetime

from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatewords

from paraserry.apps.media.models import *
from paraserry.utils.slugify import unique_slugify


class Tag(models.Model):
    """
    Abstract model defining tags shared across multiple classes
    """
    parent = models.ForeignKey('self', null = True, blank = True )
    title = models.CharField(_("Name"), max_length = 255, blank = False)
    slug = models.CharField( _("ID"), max_length = 255, 
        blank = True, unique = True )
    published = models.BooleanField( _("Published"), default = False )

    def __unicode__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)

    def update_children(self):
        [p.save() for p in self.get_children()]

    def get_children(self):
        return self.__class__.objects.filter(parent=self)

    def get_parent_root(self):
        """Used for Search Indexing to Get the Tag Class (i.e. Channels)"""
        if self.parent:
            return self.parent.get_parent_root()
        else:
            return self

    @property
    def admin_levels(self):
        if self.parent:
            return "%s&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" % self.parent.admin_levels
        else:
            return ""

    @property
    def admin_title(self):
        if self.parent:
            
            return mark_safe("%s&lfloor; %s" % (self.admin_levels, self.title))
        else:
            return self.title

    @property
    def path(self):
        if self.parent:
            return "%s%s/" % (self.parent.path, self.slug)
        else:
            return "/%s/" % self.slug

    class Meta:
        ordering = [ "title" ]

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)
        self.update_children()


class Project(models.Model):
    project_title = models.CharField(max_length=255, blank = True, null = True)
    client = models.CharField(max_length=255, blank = True, null = True)
    txtid = models.CharField( max_length = 255 )
    launch_date = models.DateField('Launched on', blank=True, null=True)
    main_url = models.URLField('URL', max_length=200, blank=True)
    about = models.TextField('About', blank=True)
    images = models.ImageField(upload_to='/images')
    tags = models.ManyToManyField(Tag, blank=True, 
        null=True, related_name="project_tags")
    created = models.DateTimeField( _("Time created"), auto_now_add = True )
    published = models.BooleanField( _("Published"), default = False )
    order = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        return reverse('project', kwargs = {'pk':self.pk })

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)


class ResumeItem(models.Model):
    title = models.CharField(max_length=255, blank = True, null = True)
    employer = models.CharField(max_length=255, blank = True, null = True)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    description = models.TextField('Description', blank=True)
    hide = models.BooleanField( _("Hide from List"), default = False )

    @property
    def get_daterange(self):
        if self.start_date and self.end_date:
            return "%s - %s" % (self.start_date.strftime("%B %Y"), self.end_date.strftime("%B %Y"))
        elif self.start_date:
            return "%s - present" % (self.start_date.strftime("%B %Y"))
        else:
            return None



    def __unicode__(self):
        return self.title

class ResumeItemDetail(models.Model):
    parent = models.ForeignKey('ResumeItem')
    description = models.TextField('Description', blank=True)
    hide = models.BooleanField( _("Hide from List"), default = False )
    order = models.PositiveIntegerField('Order', null = True, blank=True,
        help_text="Order in which this item appears in the set." )

    def __unicode__(self):
        return truncatewords(self.description, 10)

class ContentBlock( models.Model):
    project = models.ForeignKey('Project', null = True, blank = True )
    content = models.TextField('Content', blank=True)
    images = models.ManyToManyField('media.Image', blank=True, 
        null=True, related_name="contentblock_image")
    documents = models.ManyToManyField('media.Document', blank=True, 
        null=True, related_name="contentblock_document")
    order = models.PositiveSmallIntegerField()


class LinkItem( models.Model ):

    parent = models.ForeignKey('self', blank = True, null = True)
    display_name = models.CharField(_("Display Name"), max_length = 255, blank = False)

    txtid = models.CharField(_('txtid'), max_length=255, unique=True)
    order = models.PositiveIntegerField('Order', null = True,
        help_text="Order in which this link appears in the set." )

    path = models.CharField(_('path'), max_length=255)

    url = models.CharField(_("URL"), max_length = 255, blank = True,
        help_text="Enter the full path for an external link, i.e. https://www.40weeksthemovie.com/\
        or relative path for internal link, i.e. /login/" )
    hide = models.BooleanField( _("Hide from LinkSet"), default = False )

    def save(self, *args, **kwargs):
        if self.pk:
            original = self.__class__.objects.get(pk=self.pk)
        else:
            original = None

        self.path = self.generate_path()

        # -- Update path
        path_changed = (original!=None) and (original.path != self.path)       

        unique_slugify(self, self.display_name, 'txtid')
        
        #Dont let link item point to self
        if self.parent and self.parent == self:
            self.parent = None

        super(LinkItem, self).save(*args, **kwargs)

        if path_changed:
            self.update_children()   
    
    def update_children(self):
        [p.save() for p in self.get_children()]

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "display_name__icontains", "parent__display_name")

    @property
    def admin_levels(self):
        if self.parent:
            return "%s<span style='color:#fff'>|------</span>" % self.parent.admin_levels
        else:
            return ""

    @property
    def admin_title(self):
        if self.parent:
            return mark_safe("%s&lfloor; %s" % (self.admin_levels, self.display_name))
        else:
            return self.display_name

    def generate_path(self):
        if self.parent:
            return "%s%s/%s/" % (self.parent.path, self.order, self.txtid)
        else:
            return "/%s/" % self.txtid


    class Meta:
        ordering = [ 'order']
        verbose_name = "Link Item"
        verbose_name_plural = "Link Items"

   

    def __unicode__(self):
        return self.display_name

    def get_children(self):
        return self.__class__.objects.filter(parent=self)\
            .exclude(hide=True).order_by('order')

    def get_path(self):
        if self.url:
            return self.url
        else:
            if self.page:
                return self.page.get_absolute_url()
            else:
                return ''

    def get_target(self):
        if self.url:    
            if 'http' in self.url:
                return 'target=_blank'
            else:
                return ''
        else:
            return ''


