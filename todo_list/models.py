from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    _password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.username}"
    
class Task(models.Model):
    task = models.CharField(max_length=50)
    priority = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Users')

    def __str__(self) -> str:
        return f"{self.task} - {self.priority}"