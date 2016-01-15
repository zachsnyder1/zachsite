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
	A code string that is displayed as an example.
	"""
	project = models.ForeignKey(Project)
	codetext = models.TextField()

#----------------------------------------------------------
#------------ ENTITIES FOR PROJECT DOCUMENTATION: ---------
#----------------------------------------------------------
class SymbolEntity(models.Model):
	"""
	Abstract Base Class for entities that have a symbol and
	a description (module, class, method, variable...).
	"""
	symbol = models.CharField(max_length=120)
	description = models.TextField()
	orderingIndex = models.IntegerField()
	
	def __str__(self):
		return self.symbol
	
	class Meta:
		ordering = ['orderingIndex']

class ProjModule(SymbolEntity):
	"""
	Entity representing a module in a project.
	"""
	project = models.ForeignKey(Project)
	path = models.CharField(max_length=300)

class ModuleConstant(SymbolEntity):
	"""
	Entity representing a global constant in a module.
	"""
	module = models.ForeignKey(ProjModule)

class ProjClass(SymbolEntity):
	"""
	Entity representing a class in a module.
	"""
	module = models.ForeignKey(ProjModule)
	
class ConstructorParam(SymbolEntity):
	"""
	Entity representing a constructor argument for a class.
	"""
	pclass = models.ForeignKey(ProjClass)
	default = models.CharField(max_length=120, blank=True)

class ClassVariable(SymbolEntity):
	"""
	Entity representing a class variable.
	"""
	pclass = models.ForeignKey(ProjClass)

class InstanceVariable(SymbolEntity):
	"""
	Entity representing an instance variable.
	"""
	pclass = models.ForeignKey(ProjClass)

class ClassMethod(SymbolEntity):
	"""
	Entity representing a method of a class.
	"""
	pclass = models.ForeignKey(ProjClass)
	
class MethodParam(SymbolEntity):
	"""
	Entity representing an argument of a 
	"""
	method = models.ForeignKey(ClassMethod)
	default = models.CharField(max_length=120, blank=True)
	
class MethodReturn(SymbolEntity):
	"""
	Entity representing a return value of a method.
	"""
	method = models.ForeignKey(ClassMethod)
	