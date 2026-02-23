from django.db import models
from django.db.models import FileField, ImageField
from django.db.models.base import Model


# Create your models here.
class UserProfile(Model):
    image = ImageField(upload_to='images')