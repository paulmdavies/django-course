from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView

from reviews.forms import ReviewForm
from reviews.models import Review


# Create your views here.
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thanks'


class ThanksView(TemplateView):
    template_name = 'reviews/thanks.html'


class ReviewsView(ListView):
    template_name = 'reviews/reviews.html'
    model = Review
    context_object_name = 'reviews'


class ReviewDetailView(DetailView):
    model = Review
