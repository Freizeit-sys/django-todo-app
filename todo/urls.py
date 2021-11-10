from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('todo_detail/<int:pk>', views.TodoDetailView.as_view(), name='todo_detail'),
    path('todo_create', views.TodoCreateView.as_view(), name='todo_create'),
    path('todo_update', views.TodoUpdateView.as_view(), name='todo_update'),
]
