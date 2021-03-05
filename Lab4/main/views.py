from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo


def home(request):
    return HttpResponse("<h1>Привет мир<h1>")


def main(request):
    return HttpResponse('<h1>Main<h1>')

def todos(request):
    data=Todo.objects.filter(completed=False)
    return render(request,'main/todos.html',context={"todos":data})

def completedTodoList(request):
    data=Todo.objects.filter(completed=True)
    return render(request,'main/completed_todo_list.html',context={"todos":data})
