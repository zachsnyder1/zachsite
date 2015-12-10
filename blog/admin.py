from django.contrib import admin
from .models import Entry


class BlogEntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
admin.site.register(Entry, BlogEntryAdmin)