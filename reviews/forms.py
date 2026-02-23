from django.forms.models import ModelForm

from reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Review',
            'rating': 'Your Rating'
        }
