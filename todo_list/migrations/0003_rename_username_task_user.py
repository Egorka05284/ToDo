# Generated by Django 4.2 on 2025-02-06 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_rename_password_user__password_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='username',
            new_name='user',
        ),
    ]
