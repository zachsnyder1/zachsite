from django.contrib import admin
from .models import Project, CodeExample, ProjModule, ProjClass, \
	ConstructorArg, ClassVariable, InstanceVariable, ClassMethod, MethodArg, \
	MethodReturn


class ProjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
admin.site.register(Project, ProjectAdmin)
admin.site.register(CodeExample)
admin.site.register(ProjModule)
admin.site.register(ProjClass)
admin.site.register(ConstructorArg)
admin.site.register(ClassVariable)
admin.site.register(InstanceVariable)
admin.site.register(ClassMethod)
admin.site.register(MethodArg)
admin.site.register(MethodReturn)