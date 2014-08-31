import os

from paraserry import env
from paraserry.settings.base import *

#VAR_ROOT = '/srv/http/fw_media'

#Media
MEDIA_ROOT = ''
MEDIA_URL = "//%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#Static
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME