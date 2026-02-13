from django.urls import path

from bookoutlet.views import index, book_detail

urlpatterns = [
    path('', index),
    path('book/<slug:slug>', book_detail, name='book_detail')
]