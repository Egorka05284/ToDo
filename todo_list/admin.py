from django.contrib import admin

from todo_list import models

# Register your models here.
# admin.site.register(models.Users)
# admin.site.register(models.Tasks)


@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    
    list_display = ["task", "priority", "user_id"]


@admin.register(models.Users)
class UsersAdmin(admin.ModelAdmin):
    pass
