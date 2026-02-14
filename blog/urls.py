from django.urls import path

from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('posts/<slug:slug>', views.post, name='post'),
    path('author/', views.authors, name='authors'),
    path('author/<slug:slug>', views.author, name='author'),
]
