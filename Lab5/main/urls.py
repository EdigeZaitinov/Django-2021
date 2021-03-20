from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('todos', views.todos, name='todos'),
    path('completed_todos',views.completedTodoList,name='completedTodos'),
    path('<int:todo_id>/completed_todos',views.getCompletedTodoById,name='completedTodoById'),
]
