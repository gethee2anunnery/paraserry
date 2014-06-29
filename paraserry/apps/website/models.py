from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=200, blank = True, null = True)
    launch_date = models.DateField('Launched on', blank=True)
    main_url = models.URLField('URL', max_length=200, blank=True)
    about = models.TextField('About', blank=True)
    images = models.ImageField(upload_to='/images')
    created = models.DateTimeField( _("Time created"), auto_now_add = True )