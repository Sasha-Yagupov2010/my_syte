from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    return render(request, "index.html", context)

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Используем кастомную форму
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Перенаправляем на главную
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def registr_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Автоматически логиним после регистрации
            return redirect('index')  # Перенаправляем на главную
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = RegisterForm()
    return render(request, 'registr.html', {'form': form})
    



@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user  # автоматически ставим текущего пользователя
            task.save()
            return redirect('index')  # или куда нужно
    else:
        form = TaskForm()
    
    return render(request, 'tasks/createTask.html', {'form': form})    


def task_list(request):

    return render(request, 'tasks/taskList.html')   