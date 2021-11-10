from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo

class TodoListView(ListView):
    model = Todo
    context_object_name = 'tasks'
    
class TodoDetailView(DetailView):
    model = Todo
    context_object_name = 'task'
    
class TodoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('todo_list')
    
class TodoUpdateView(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('todo_list')
    
class TodoDeleteView(DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('todo_list')