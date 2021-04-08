from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model() # 현재프로젝트의 엑티브된 유저를 지칭 : accounts.User
        fields = UserCreationForm.Meta.fields 


class IngredientChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('hateingredient', )