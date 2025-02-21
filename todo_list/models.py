from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser):

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return f"{self.username}"


class Tasks(models.Model):
    
    task = models.CharField(max_length=150)
    priority = models.PositiveSmallIntegerField(default=1, db_index=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="Users")

    def __str__(self) -> str:
        return f"{self.task} - {self.priority}"

    class Meta:
        db_table = "task"
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ("-priority",)
