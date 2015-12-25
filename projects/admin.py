from django.contrib import admin
from .models import Project, CodeExample, ProjModule, ProjClass, \
	ConstructorParam, ClassVariable, InstanceVariable, ClassMethod, \
	MethodParam, MethodReturn


class ProjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
admin.site.register(Project, ProjectAdmin)
admin.site.register(CodeExample)
admin.site.register(ProjModule)
admin.site.register(ProjClass)
admin.site.register(ConstructorParam)
admin.site.register(ClassVariable)
admin.site.register(InstanceVariable)
admin.site.register(ClassMethod)
admin.site.register(MethodParam)
admin.site.register(MethodReturn)