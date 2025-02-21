from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from todo_list.forms import NewTaskForm, UserLoginForm, UserSignupForm
from todo_list.models import Users, Tasks


# Create your views here.
def index(request):

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                # messages.success(request, f"{user.username}, You signed in successfully")
                return HttpResponseRedirect(reverse("todo_list:todo"))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "todo_list/index.html", context)


def todo(request):
    if not request.user.is_authenticated:
        return redirect(reverse("todo_list:index"))
    user = request.user
    user_id = Users.objects.filter(username=user).values_list("id", flat=True).first()
    tasks = Tasks.objects.filter(user_id=user_id)
    return render(
        request,
        "todo_list/todo.html",
        {
            "tasks": tasks,
        },
    )


def signup(request):

    if request.method == "POST":
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("todo_list:todo"))
    else:
        form = UserSignupForm()

    context = {"form": form}
    return render(request, "todo_list/signup.html", context)


@login_required
def logout(request):
    # messages.success(request, f"{request.user.username}, You logged out")
    auth.logout(request)
    return redirect(reverse("todo_list:index"))


def add_task(request):

    if not request.user.is_authenticated:
        return redirect(reverse("todo_list:index"))
    form = NewTaskForm()
    if request.method == "GET":
        form = NewTaskForm()

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            object = Tasks()
            object.task = form["task"]
            object.priority = form["priority"]
            object.user_id = (
                Users.objects.filter(username=request.user)
                .values_list("id", flat=True)
                .first()
            )
            object.save()
            return redirect(reverse("todo_list:todo"))
    return render(request, "todo_list/addtask.html", {"form": form})


def remove_task(request, task_id):

    task = Tasks.objects.get(id=task_id)
    task.delete()

    return redirect(request.META["HTTP_REFERER"])
