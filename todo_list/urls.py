from django.urls import path
from todo_list import views

app_name = "todo_list"

urlpatterns = [
    path("login", views.UserLoginView.as_view(), name="index"),
    path("todo", views.TodoView.as_view(), name="todo"),
    path("signup", views.UserSignUpView.as_view(), name="signup"),
    path("logout", views.logout, name="logout"),
    path("add_task", views.add_task, name="add_task"),
    path("remove_task/<int:task_id>/", views.remove_task, name="remove_task"),
]
