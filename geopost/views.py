import base64
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import GeoPostForm
from .models import GeoPost
from .view_helper import upload_to_bucket, rollback_upload, post_geometry, \
	download_from_bucket

# Create your views here.
class Home(View):
	"""
	The Geopost homepage view class.
	"""
	def get(self, request):
		"""
		The GET view method.
		"""
		form = GeoPostForm()
		return render(request, 'geopost/home_anonymous.html', { 'form': form })

class CreateOrEdit(View):
	"""
	The GeoPost view class for editing or creating a new post.
	"""
	def get(self, request):
		"""
		Return form...
		"""
		pass
