from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('create', views.create_todo, name="create-todo"),
    path('detail/<id>', views.todo_detail, name="todo-detail"),
    path('delete/<id>', views.todo_delete, name="todo-delete"),
    path('edit/<id>', views.todo_edit, name="edit-todo"),
]