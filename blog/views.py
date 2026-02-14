from datetime import date

from django.shortcuts import render

from blog.models import Post


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
