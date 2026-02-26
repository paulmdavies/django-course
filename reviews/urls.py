from django.urls import path

from reviews.views import ReviewView, ThanksView, ReviewsView, ReviewDetailView, ReviewFavouriteView

urlpatterns = [
    path('', ReviewView.as_view()),
    path('thanks', ThanksView.as_view()),
    path('reviews', ReviewsView.as_view()),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/favourite', ReviewFavouriteView.as_view())
]