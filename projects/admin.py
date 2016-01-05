from django.contrib import admin
from .models import Project, CodeExample, ProjModule, ProjClass, \
	ConstructorParam, ClassVariable, InstanceVariable, ClassMethod, \
	MethodParam, MethodReturn

# INLINES:
class CodeExampleInline(admin.TabularInline):
	model = CodeExample
	extra = 0

class ProjModuleInline(admin.TabularInline):
	model = ProjModule
	extra = 0
	
class ProjClassInline(admin.TabularInline):
	model = ProjClass
	fk_name = 'module'
	extra = 0

class ConstructorParamInline(admin.TabularInline):
	model = ConstructorParam
	fk_name = 'pclass'
	extra = 0

class ClassVariableInline(admin.TabularInline):
	model = ClassVariable
	fk_name = 'pclass'
	extra = 0

class InstanceVariableInline(admin.TabularInline):
	model = InstanceVariable
	fk_name = 'pclass'
	extra = 0

class ClassMethodInline(admin.TabularInline):
	model = ClassMethod
	fk_name = 'pclass'
	extra = 0

class MethodParamInline(admin.TabularInline):
	model = MethodParam
	fk_name = 'method'
	extra = 0

class MethodReturnInline(admin.TabularInline):
	model = MethodReturn
	fk_name = 'method'
	extra = 0

# Custom representations:
class ProjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	inlines = [ProjModuleInline, CodeExampleInline]

class ProjModuleAdmin(admin.ModelAdmin):
	inlines = [
		ProjClassInline
	]

class ProjClassAdmin(admin.ModelAdmin):
	inlines = [
		ConstructorParamInline, 
		ClassVariableInline,
		InstanceVariableInline,
		ClassMethodInline
	]

class ClassMethodAdmin(admin.ModelAdmin):
	inlines = [
		MethodParamInline,
		MethodReturnInline
	]

# Registrations:
admin.site.register(Project, ProjectAdmin)
admin.site.register(CodeExample)
admin.site.register(ProjModule, ProjModuleAdmin)
admin.site.register(ProjClass, ProjClassAdmin)
admin.site.register(ConstructorParam)
admin.site.register(ClassVariable)
admin.site.register(InstanceVariable)
admin.site.register(ClassMethod, ClassMethodAdmin)
admin.site.register(MethodParam)
admin.site.register(MethodReturn)
