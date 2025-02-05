from django.contrib import admin

from todo_list import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Task)