from django.shortcuts import render
from django.http import HttpResponse
import json


def home(request):
    return HttpResponse("<h1>Привет мир<h1>")


def main(request):
    return HttpResponse('<h1>Main<h1>')

def todos(request):
    jsonData=open('static/todos.json','r').read()
    data=json.loads(jsonData)
    return render(request,'main/todos.html',context={"todos":data})

def completedTodoList(request):
    jsonData=open('static/completed_todos.json','r').read()
    data=json.loads(jsonData)
    return render(request,'main/completed_todo_list.html',context={"todos":data})
