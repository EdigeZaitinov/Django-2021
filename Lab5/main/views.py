from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from users.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.core import serializers


@login_required(login_url='login')
def home(request):
    date = datetime.now().date()
    return render(request, 'main/home.html', context={"today": date})


def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Email or password is incorrect")
    context = {}
    return render(request, 'main/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('login')


def registration(request):
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, 'аккаунт был создан для '+email)
    return render(request, 'main/registration.html', context={"form": form})

@login_required(login_url='login')
def todos(request):
    data = Todo.objects.filter(completed=False)
    return render(request, 'main/todos.html', context={"todos": data})

@login_required(login_url='login')
def completedTodoList(request):
    data = Todo.objects.filter(completed=True)
    return render(request, 'main/completed_todo_list.html', context={"todos": data})

@login_required(login_url='login')
def getCompletedTodoById(request,todo_id):
    todo=Todo.objects.filter(completed=True,number=todo_id)
    data = serializers.serialize('json', todo)
    return HttpResponse(data)
