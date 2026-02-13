from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from bookoutlet.models import Book, Author, Address, Country


# Register your models here.

class BookAdmin(ModelAdmin):
    list_filter = [
        'rating',
        'author'
    ]

    list_display = [
        'title',
        'author'
    ]

    prepopulated_fields = {
        'slug': ['title']
    }


class AuthorAdmin(ModelAdmin):
    list_display = [
        'last_name',
        'first_name'
    ]


class CountryAdmin(ModelAdmin):
    list_display = [
        'name',
        'code'
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country, CountryAdmin)