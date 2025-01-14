# Generated by Django 5.1.2 on 2024-10-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_task_description_en_task_description_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_tr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_tr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
