from django.conf.urls.static import static
from django.conf.urls import patterns, url, include

from .views import *

urlpatterns = patterns('',
      
    url(r'admin/media/image_mediapicker$', ImageMediaPicker.as_view(), name="admin_image_media_mediapicker"), 
)