from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from base.models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/tasks.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    pass