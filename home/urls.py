from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('todos/',views.todos.as_view(),name="todos"), 
    path('todo/<int:pk>',views.todo.as_view(),name="todo"), 
]
