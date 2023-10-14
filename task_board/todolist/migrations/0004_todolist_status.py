# Generated by Django 4.1.4 on 2023-10-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_todolist_text2'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'Inprogress'), ('Done', 'Done')], default='New', max_length=45),
        ),
    ]