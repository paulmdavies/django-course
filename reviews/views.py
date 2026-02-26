from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['is_favourite'] = self.object.id == int(self.request.session.get('favourite_review'))

        return context_data


class ReviewFavouriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favourite_review'] = review_id

        return HttpResponseRedirect(f'/review/{review_id}')