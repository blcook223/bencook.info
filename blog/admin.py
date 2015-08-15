from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'tags', 'body']
    list_display = ['title', 'date']


class TagAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
