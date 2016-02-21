import base64
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .forms import GeoPostForm
from .models import GeoPost
from projects.models import Project
from .view_helper import upload_to_bucket, rollback_upload, post_geometry, \
	download_from_bucket

class GeoPostBase(View):
	"""
	The Geopost base view class...
	"""
	subnav_location = 'projects/geopost/subnav.html'
	curr_project = get_object_or_404(Project, slug='geopost')

# Create your views here.
class Home(GeoPostBase):
	"""
	The Geopost homepage view class.
	"""
	def get(self, request):
		"""
		The GET view method.
		"""
		form = GeoPostForm()
		projectList = Project.objects.all().filter(active=True).order_by("title")
		context = {
			'form': form,
			'projectList': projectList,
			'subnav_location': self.subnav_location,
			'curr_project': self.curr_project
		}
		return render(request, 'geopost/home_anonymous.html', context)

class CreatePost(GeoPostBase):
	"""
	The GeoPost view class for creating a new post.
	"""
	def get(self, request):
		"""
		Render with blank form...
		"""
		form = GeoPostForm()
		projectList = Project.objects.all().filter(active=True).order_by("title")
		context = {
			'form': form,
			'projectList': projectList,
			'subnav_location': self.subnav_location,
			'curr_project': self.curr_project
		}
		return render(request, 'geopost/create.html', context)
	
	def post(self, request):
		"""
		Process newly submitted GeoPost entry...
		"""
		uuid = request.POST['uuid']
		title = request.POST['title']
		body = request.POST['body']
		photo = request.FILES['photo'] # FOR STORAGE
		wfsxml = request.POST['wfsxml'] # FOR GEOSERVER
		data = {
			'uuid': uuid,
			'title': title,
			'body': body,
			'wfsxml': wfsxml
		}
		form = GeoPostForm(data)
		# Validate form --> upload photo to bucket --> post XML to geoserver
		# NO VALIDATION ERROR
		if form.is_valid():
			# use clean values
			uuid = form.cleaned_data['uuid']
			wfsxml = form.cleaned_data['wfsxml']
			photo.open('rb')
			error = upload_to_bucket(photo, 'zachtestbucket', photo.content_type, uuid)
			photo.close()
			# NO UPLOAD ERROR
			if not error:
				error = post_geometry(wfsxml, "http://127.0.0.1:8080/geoserver/wfs")
				# ALL GOOD
				if not error:
					return HttpResponseRedirect(reverse('geopost_home'))
				# ERROR POSTING TO GEOSERVER
				else:
					rollback_upload(uuid, 'zachtestbucket')
					resp = HttpResponse(status=502)
					resp.write("<h3>502 BAD GATEWAY: </h3>")
					resp.write("<p>WFS ERROR {}</p>".format(error))
					return resp
			# ERROR UPLOADING IMAGE
			else:
				resp = HttpResponse(status=502)
				resp.write("<h3>502 BAD GATEWAY: </h3>")
				resp.write("<p>IMAGE UPLOAD ERROR: {}</p>".format(error))
				return resp
		# FORM VALIDATION ERROR
		else:
			projectList = Project.objects.all().filter(active=True).order_by("title")
			context = {
				'form': form,
				'projectList': projectList,
				'subnav_location': self.subnav_location,
				'curr_project': self.curr_project
			}
			return render(request, 'geopost/create.html', context)
		
class EditPost(GeoPostBase):
	"""
	The GeoPost view class for editing an existing post.
	"""
	def get(self, request, entry_uuid):
		"""
		Get the form...
		"""
		form = GeoPostForm()
		projectList = Project.objects.all().filter(active=True).order_by("title")
		context = {
			'form': form,
			'projectList': projectList,
			'subnav_location': self.subnav_location,
			'curr_project': self.curr_project
		}
		return render(request, 'geopost/edit.html', context)
	
	def Post(self, request, entry_uuid):
		"""
		Process the edited entry fields...
		"""
		pass

def photo(request, entry_uuid):
	"""
	The GeoPost view method for retrieving photos
	"""	
	if request.method == "GET":
		resp = HttpResponse()
		metadata, photo = download_from_bucket(entry_uuid, 'zachtestbucket')
		resp.write(base64.b64encode(photo))
		resp['Content-Type'] = metadata['contentType']
		return resp
