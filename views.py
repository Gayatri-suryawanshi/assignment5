from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import RegisterForm


def home(request):
    return render(request, 'login/home.html')


def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', { 'form' : form })