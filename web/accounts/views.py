from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm, IngredientChangeForm
from django.contrib.auth.decorators import login_required
from foods.models import Ingredient
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('foods:index')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'foods:index')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('foods:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:mypage')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:mypage')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)

@login_required
def mypage(request):
    # user가 올린 음식 데이터들이 필요
    return render(request, 'accounts/mypage.html')


def change_food(request):
    # user_ingredients = request.user
    # print(request.user.hateingredient)
    if request.method == "POST":
        form = IngredientChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:mypage')
    else:
        ingres = Ingredient.objects.all().order_by('name')
        context = {'ingres':ingres}
    return render(request, 'accounts/select_ingredient.html', context)

# @login_required
# def select_genre(request):
#     # select genres
#     user_prefers = request.user.genre_prefers.all()
#     if request.method == 'POST':
#         if len(user_prefers.all()):
#             for pre_value in user_prefers:
#                 genre = get_object_or_404(Genre, pk=pre_value.pk)
#                 genre.user_prefers.remove(request.user)
#             genres = Genre.objects.all()
#             context = {'genres': genres,}
#             return render(request, 'movies/select_genre.html', context)  
#         check_var = request.POST.getlist('checks')
#         if check_var:
#             for value in check_var:
#                 value = int(value)
#                 genre = get_object_or_404(Genre, pk=value)
#                 genre.user_prefers.add(request.user)
#         return redirect('movies:index')
#     else:
#         if user_prefers:
#             return redirect('movies:index')
#         genres = Genre.objects.all()
#         context = {'genres': genres,}
#         return render(request, 'movies/select_genre.html', context)