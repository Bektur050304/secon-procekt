# Generated by Django 5.1.2 on 2024-10-27 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]