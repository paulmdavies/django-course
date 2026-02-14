from datetime import date

from django.shortcuts import render

from blog.models import Post, Author


# Create your views here.
def home(request):
    all_posts = Post.objects.all().order_by('date')
    post_slice = len(all_posts) - 3

    return render(
        request,
        'blog/home.html',
        {
            'posts': all_posts[post_slice:]
        }
    )

def posts(request):
    return render(
        request,
        'blog/posts.html',
        {
            'title': 'All Posts',
            'posts': Post.objects.all().order_by('date')
        }
    )

def post(request, slug):
    return render(
        request,
        'blog/post.html',
        {
            'post': Post.objects.get(slug=slug)
        }
    )

def authors(request):
    authors = Author.objects.all()

    return render(
        request,
        'blog/authors.html',
        {
            'authors': authors
        }
    )

def author(request, slug):
    author = Author.objects.get(slug=slug)
    posts_by_author = author.posts.all().order_by('date')

    return render(
        request,
        'blog/posts.html',
        {
            'title': f'Posts by {author.first_name} {author.last_name}',
            'posts': posts_by_author
        }
    )
