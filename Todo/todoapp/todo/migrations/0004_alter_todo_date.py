# Generated by Django 4.2 on 2023-05-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_sr_no_todo_sno_alter_todo_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]