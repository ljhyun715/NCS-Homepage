from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

from .forms import UserCreationForm, UserChangeForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home:index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'account/login.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'account/signup.html', context)
