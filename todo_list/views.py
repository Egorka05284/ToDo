from django.shortcuts import render
from todo_list.models import User

# Create your views here.
def index(request):
    return render(request, 'todo_list/index.html', {
        'users': User.objects.all()
    })