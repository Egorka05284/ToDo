from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from todo_list.forms import UserLoginForm, UserSignupForm
from todo_list.models import Users, Tasks

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('todo_list:todo'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'todo_list/index.html', context)

# @login_required
def todo(request):
    # user = User.objects.get(id=username)
    if not request.user.is_authenticated:
        return redirect(reverse('todo_list:index'))
    tasks = Tasks.objects.all() 
    return render(request, 'todo_list/todo.html', {
        'tasks': tasks,
    })

def signup(request):

    if request.method == 'POST':
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('todo_list:todo'))
    else:
        form = UserSignupForm()

    context = {'form': form}
    return render(request, 'todo_list/signup.html', context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, You logged out")
    auth.logout(request)
    return redirect(reverse('todo_list:index'))