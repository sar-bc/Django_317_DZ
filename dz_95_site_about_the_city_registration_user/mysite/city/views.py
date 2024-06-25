from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError
from city.models import Posts


# Create your views here.
def index(request):
    posts = Posts.objects.all()
    context = {
        'title': 'Главная',
        'posts': posts,
    }
    return render(request, 'city/index.html', context=context)


def show_post(request, id):
    post = get_object_or_404(Posts, id=id)
    post.views += 1
    post.save(update_fields=['views'])
    return render(request, 'city/show_post.html', {'post': post})


def registration(request):
    if request.method == "GET":
        return render(request, 'city/registration.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'city/registration.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует. Задайте другое'})
        else:
            return render(request, 'city/registration.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпадают'})

def logoutuser(request):
    # if request.method == "POST":
    logout(request)
    return redirect('home')

def loginuser(request):
    if request.method == "GET":
        return render(request, 'city/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'city/login.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('home')
