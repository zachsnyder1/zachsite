from django.db import models


class Project(models.Model):
	"""
	My Projects.
	"""
	title = models.CharField(max_length=30)
	slug = models.SlugField(max_length=30)
	active = models.BooleanField(default=True)
	summary = models.TextField()
	
	def __str__(self):
		return self.title

class CodeExample(models.Model):
	"""
	A code string that is meant as an example.
	"""
	project = models.ForeignKey(Project)
	codetext = models.TextField()


"""
class ProjectClass(models.Model):
	pass

class ClassMethod(models.Model):
	pass

class ClassVariable(models.Model):
	pass

class InstanceVariable(models.Model):
	pass
"""