from django.views.generic import ListView

from .models import Todo


class TodoListView(ListView):
    model = Todo