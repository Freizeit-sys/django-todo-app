from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('todo_detail/<int:pk>', views.TodoDetailView.as_view(), name='todo_detail'),
]
