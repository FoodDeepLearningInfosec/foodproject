from django import forms
from .models import FoodInfo


class FoodCreateForm(forms.ModelForm):
    class Meta:
        model = FoodInfo
        fields = ('img',)