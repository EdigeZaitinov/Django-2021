from django.urls import path
from main import views

urlpatterns = [
    path('', views.main, name='main'),
    path('todos', views.todos, name='todos'),
    path('completed_todos',views.completedTodoList,name='completedTodos'),
]
