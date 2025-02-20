from django.urls import path
from todo_list import views

app_name = 'todo_list'

urlpatterns = [
    path('login', views.index, name="index"),
    path('todo', views.todo, name="todo"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name='logout'),
    path('add_task', views.add_task, name='add_task')
]
