from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, BooleanField, SlugField
from django.db.models.fields.related import ForeignKey, OneToOneField, ManyToManyField
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Country(Model):
    name = CharField(max_length=100)
    code = CharField(max_length=2)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Countries'


class Address(Model):
    street = CharField(max_length=100)
    city = CharField(max_length=100)
    postcode = CharField(max_length=10)

    def __str__(self):
        return f'{self.street}, {self.city}, {self.postcode}'

    class Meta:
        verbose_name_plural = 'Addresses'


class Author(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)

    address = OneToOneField(Address, on_delete=CASCADE, null=True)

    slug = SlugField(default='', null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(Model):
    title = CharField(max_length=100)
    rating = IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = ForeignKey(Author, on_delete=CASCADE, null=True, related_name='books')
    is_bestselling = BooleanField(default=False)
    slug = SlugField(default='', null=False)

    published_countries = ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])

    def __str__(self):
        return f'{self.title} (r: {self.rating})'
