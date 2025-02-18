from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from todo_list.models import Users, Tasks

# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse("index"))
    return render(request, 'todo_list/index.html')

def todo(request):
    # user = User.objects.get(id=username)
    tasks = Tasks.objects.all() 
    return render(request, 'todo_list/todo.html', {
        'tasks': tasks,
        # 'user': user
    })

def signup(request):
    return render(request, 'todo_list/signup.html')