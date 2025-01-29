from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    return render(request, 'pages/index.html')


def rent(request):
    return render(request, 'pages/rent.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pages/index.html')
        else:
            return render(request, 'pages/signin.html', {
                'error': 'Неправильный логин или пароль'
            })
    return render(request, 'pages/signin.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password-1')
        password_confirm = request.POST.get('password-2')

        if password != password_confirm:
            return render(request, 'pages/signup.html', {
                'error': 'Пароли не совпадают'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'pages/signup.html', {
                'error': 'Пользователь с таким именем уже существует'
            })

        user = User.objects.create_user(username=username, password=password)
        user.save()

        login(request, user)
        return redirect('index')
    return render(request, 'pages/signup.html')


def logout_view(request):
    logout(request)
    return redirect('index')
