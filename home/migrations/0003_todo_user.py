# Generated by Django 4.1.2 on 2023-01-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_todo_delete_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='User',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
