from datetime import date

from django.shortcuts import render

from blog.models import Post, Author, Tag


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
    post = Post.objects.get(slug=slug)

    return render(
        request,
        'blog/post.html',
        {
            'post': post,
            'tags': post.tag.all()
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

def tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    posts_with_tag = tag.posts.all().order_by('date')

    return render(
        request,
        'blog/posts.html',
        {
            'title': f'Posts tagged {tag.caption}',
            'posts': posts_with_tag
        }
    )
