# Generated by Django 4.2 on 2025-02-18 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_alter_tasks_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ('-priority',), 'verbose_name': 'task', 'verbose_name_plural': 'tasks'},
        ),
    ]
