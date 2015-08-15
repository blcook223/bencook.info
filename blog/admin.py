"""
Admin configuration for blog app
"""
from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    """
    Administrative interface for Post
    """
    fields = ['title', 'slug', 'tags', 'body']
    list_display = ['title', 'date']


class TagAdmin(admin.ModelAdmin):
    """
    Administrative interface for Tag
    """
    fields = ['name', 'slug']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
