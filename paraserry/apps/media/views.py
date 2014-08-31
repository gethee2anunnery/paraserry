from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.views.generic import ListView


from .models import *

from django.db.models import Q


class ImageMediaPicker(ListView):
	model = Image
	template_name = "admin/mediapicker.html"
	paginate_by = 48
	
	def get_queryset(self):
		
		if 'q' in self.request.GET and self.request.GET['q']!= '':
			query = self.request.GET['q']
			print "APPLLY FILTER %s"%(query)
			#return queryset.order_by('-published_time')
			queryset = Image.objects.filter(
				Q(title__icontains=query) | 
				Q(caption__icontains=query) | 
				Q(credit__icontains=query) | 
				Q(admin_description__icontains=query) ).order_by('-id')	   
		else:
			queryset = Image.objects.all().order_by('-id')
			#queryset = super(ImageMediaPicker, self).get_queryset()

		return queryset

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ImageMediaPicker, self).dispatch(*args, **kwargs)