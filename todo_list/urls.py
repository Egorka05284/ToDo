from django.urls import path
from todo_list import views


urlpatterns = [
    path('', views.index, name='index')
]