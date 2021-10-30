from datetime import date, timedelta, datetime

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm, UserCreateForm, UserProfileForm


def login(request):
    today = datetime.now() + timedelta(hours=5)
    today = date(today.year, today.month, today.day)
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {'page_title': 'авторизация',
               'form': form,
               'today': today,
               }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    today = datetime.now() + timedelta(hours=5)
    today = date(today.year, today.month, today.day)
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserCreateForm()

    context = {'page_title': 'регистрация',
               'form': form,
               'today': today,
               }
    return render(request, 'authapp/register.html', context)


def profile(request):
    today = datetime.now() + timedelta(hours=5)
    today = date(today.year, today.month, today.day)
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES,
                               instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {'page_title': 'профиль',
               'form': form,
               'today': today,
               }
    return render(request, 'authapp/profile.html', context)
