from django.db import models


class Project(models.Model):
    """
    My Projects.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    active = models.BooleanField(default=True)
    has_docs = models.BooleanField(default=True)
    logo = models.CharField(max_length=30)
    summary = models.TextField()

    def __str__(self):
        return self.title


class CodeExample(models.Model):
    """
    A code string that is displayed as an example.
    """
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    codetext = models.TextField()

#----------------------------------------------------------
#------------ ENTITIES FOR PROJECT DOCUMENTATION: ---------
#----------------------------------------------------------


class SymbolEntity(models.Model):
    """
    Abstract Base Class for entities that have a symbol and
    a description (module, class, method, variable...).
    """
    id = models.AutoField(primary_key=True)
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    path = models.CharField(max_length=300)


class ModuleConstant(SymbolEntity):
    """
    Entity representing a global constant in a module.
    """
    module = models.ForeignKey(ProjModule, on_delete=models.CASCADE)


class ProjClass(SymbolEntity):
    """
    Entity representing a class in a module.
    """
    module = models.ForeignKey(ProjModule, on_delete=models.CASCADE)


class ConstructorParam(SymbolEntity):
    """
    Entity representing a constructor argument for a class.
    """
    pclass = models.ForeignKey(ProjClass, on_delete=models.CASCADE)
    default = models.CharField(max_length=120, blank=True)


class ClassVariable(SymbolEntity):
    """
    Entity representing a class variable.
    """
    pclass = models.ForeignKey(ProjClass, on_delete=models.CASCADE)


class InstanceVariable(SymbolEntity):
    """
    Entity representing an instance variable.
    """
    pclass = models.ForeignKey(ProjClass, on_delete=models.CASCADE)


class ClassMethod(SymbolEntity):
    """
    Entity representing a method of a class.
    """
    pclass = models.ForeignKey(ProjClass, on_delete=models.CASCADE)


class MethodParam(SymbolEntity):
    """
    Entity representing an argument of a 
    """
    method = models.ForeignKey(ClassMethod, on_delete=models.CASCADE)
    default = models.CharField(max_length=120, blank=True)


class MethodReturn(SymbolEntity):
    """
    Entity representing a return value of a method.
    """
    method = models.ForeignKey(ClassMethod, on_delete=models.CASCADE)
