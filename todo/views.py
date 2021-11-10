from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Todo

class TodoListView(ListView):
    model = Todo
    content_object_name = 'tasks'
    
class TodoDetailView(DetailView):
    model = Todo
    context_object_name = 'task'