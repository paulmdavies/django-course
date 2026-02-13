from django.db.models import Avg
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from bookoutlet.models import Book


# Create your views here.
def index(request):
    books = Book.objects.all().order_by('title')

    return render(
        request,
        'bookoutlet/index.html',
        {
            'books': books,
            'book_count': books.count(),
            'average_rating': books.aggregate(Avg('rating'))['rating__avg']
        },
    )


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(
        request,
        'bookoutlet/book_detail.html',
        {
            'book': book
        },
    )