from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from blog.models import Author, Tag, Post

# Register your models here.
class PostAdmin(ModelAdmin):
    list_display = [
        'title',
        'author',
        'date'
    ]

    list_filter = [
        'author',
        'tags',
        'date'
    ]

    prepopulated_fields = {
        'slug': ['title']
    }


class AuthorAdmin(ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email'
    ]

    prepopulated_fields = {
        'slug': ['first_name', 'last_name']
    }


class TagAdmin(ModelAdmin):
    list_display = [
        'caption'
    ]

    prepopulated_fields = {
        'slug': ['caption']
    }

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
