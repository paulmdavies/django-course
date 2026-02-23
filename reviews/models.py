from django.db import models
from django.db.models import Model
from django.db.models.fields import CharField, TextField, IntegerField


# Create your models here.
class Review(Model):
    user_name = CharField(max_length=100)
    review_text = TextField()
    rating = IntegerField()

    def _get_star_rating(self):
        return ('★' * self.rating).ljust(5, '☆')

    star_rating = property(_get_star_rating)