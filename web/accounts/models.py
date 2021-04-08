from django.db import models
from django.contrib.auth.models import AbstractUser
from foods.models import Ingredient


# Create your models here.
class User(AbstractUser):
    hateingredient = models.ManyToManyField(Ingredient, related_name='hatepeople', blank=True)
