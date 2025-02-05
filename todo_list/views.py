from django.shortcuts import render
from todo_list.models import User, Task

# Create your views here.
def index(request):
    return render(request, 'todo_list/index.html', {
        'tasks': Task.objects.all()
    })