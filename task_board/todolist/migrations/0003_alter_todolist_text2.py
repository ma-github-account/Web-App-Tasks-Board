# Generated by Django 4.1.4 on 2023-10-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_text2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='text2',
            field=models.CharField(max_length=45),
        ),
    ]
