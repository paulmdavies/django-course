from django.urls import path

from reviews.views import review

urlpatterns = [
    path('', review)
]