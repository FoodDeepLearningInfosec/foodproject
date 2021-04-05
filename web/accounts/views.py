from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .froms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):

    # if request.uesr.is_authenticated:
    #     return redirect('foods:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('foods:index')
    else:
        form = UserCreationForm()
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
        form = CustomUserChangeForm(request.POST, isinstance=request.user)
        if form.is_valid():
            form.save()
            return redirect('foods:index')
    else:
        form = CustomUserChangeForm(isinstance=request.user)
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)


def change_password(request):
    if request.method == 'POST':
        pass
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/change_password.html', context)
