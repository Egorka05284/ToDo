from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from todo_list.models import Tasks, Users


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        required=True,
        label="Username",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Enter your username",
                "class": "form-control",
                "name": "username",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "placeholder": "Enter your password",
                "class": "form-control",
                "name": "password",
            }
        ),
    )

    class Meta:
        model = Users
        fields = ["username", "password"]


class UserSignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = (
            "username",
            "password1",
            "password2",
        )

    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class NewTaskForm(forms.Form):
    class Meta:
        model = Tasks
        fields = ["task", "priority"]

    task = forms.CharField(
        label="Task",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter new task", "name": "task"}),
    )
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
