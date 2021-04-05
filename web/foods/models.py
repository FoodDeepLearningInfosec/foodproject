from django.db import models
from django.conf import settings

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=140)
    
class FoodCategory(models.Model):
    name = models.CharField(max_length=140)

class Food(models.Model):
    name = models.CharField(max_length=140)
    ingredients = models.ManyToManyField(Ingredient, related_name='foods')
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)

