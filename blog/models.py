from django.db import models
from django.db.models import Model, CharField, DateField, SlugField, CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField


# Create your models here.
class Author(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = CharField(max_length=100)

    slug = SlugField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(Model):
    caption = CharField(max_length=100)


class Post(Model):
    title = CharField(max_length=1000, null=False)
    summary = CharField(max_length=1000, null=False)
    content = CharField(max_length=10000, null=False)
    image_name = CharField(max_length=100, null=False)
    date = DateField(auto_now_add=True)
    slug = SlugField(null=False)

    author = ForeignKey(Author, on_delete=CASCADE)
    tag = ManyToManyField(Tag, related_name='tags', blank=True)

