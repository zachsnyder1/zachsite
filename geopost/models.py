from django.db import models

# Create your models here.
class GeoPost(models.Model):
	"""
	Tablespace for GeoPost posts.
	"""
	uuid = models.UUIDField(primary_key=True, editable=False)
	title = models.CharField(max_length=30)
	body = models.TextField()
	pub_time = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.title

	