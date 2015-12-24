from django.contrib import admin
from .models import Project, CodeExample


class ProjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
admin.site.register(Project, ProjectAdmin)
admin.site.register(CodeExample)