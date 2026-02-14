from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from blog.models import Author, Tag, Post

# Register your models here.
class PostAdmin(ModelAdmin):
    list_display = [
        'title',
        'author',
        'slug'
    ]

    list_filter = [
        'author'
    ]

    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
