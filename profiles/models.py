from django.db import models
from django.db.models import FileField
from django.db.models.base import Model


# Create your models here.
class UserProfile(Model):
    image = FileField(upload_to='images')