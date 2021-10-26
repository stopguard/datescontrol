from datetime import date, timedelta, datetime

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm


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
    pass


def register(request):
    pass
