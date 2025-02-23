from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView
from todo_list.forms import NewTaskForm, UserLoginForm, UserSignupForm
from todo_list.models import Users, Tasks


# Create your views here.


class TodoView(TemplateView):
    
    template_name = "todo_list/todo.html"

    def get(self, request, *args, **kwargs) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect(reverse('todo_list:index'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict:
        
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_id = Users.objects.filter(username=user).values_list("id", flat=True).first()
        tasks = Tasks.objects.filter(user_id=user_id)
        context['tasks'] = tasks
        
        return context


class UserLoginView(LoginView):

    template_name = 'todo_list/index.html'
    form_class = UserLoginForm
    next_page = reverse_lazy('todo_list:todo')



class UserSignUpView(CreateView):
    template_name = 'todo_list/signup.html'
    form_class = UserSignupForm
    success_url = reverse_lazy('todo_list:todo')

    def form_valid(self, form):
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)
            return redirect(self.success_url)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("todo_list:index"))

class TaskAddView(FormView):
    template_name = 'todo_list/add_task.html'
    form_class = NewTaskForm

    def get(self, request) -> HttpResponse:
        if not self.request.user.is_authenticated:
            return redirect(reverse('todo_list:index'))
        form = NewTaskForm()

        return render(self.request, "todo_list/addtask.html", {"form": form})

    def form_valid(self, form):
        form = form.cleaned_data
        object = Tasks()
        object.task = form["task"]
        object.priority = form["priority"]
        object.user_id = (
            Users.objects.filter(username=self.request.user)
            .values_list("id", flat=True)
            .first()
        )
        object.save()
        return redirect(reverse("todo_list:todo"))
    

class TaskDeleteView(TemplateView):
    
    def get(self, request, task_id):
        task = Tasks.objects.get(id=task_id)
        task.delete()

        return redirect(self.request.META["HTTP_REFERER"])
