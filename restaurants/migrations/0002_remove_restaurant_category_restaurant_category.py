# Generated by Django 5.0.2 on 2024-06-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='category',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ManyToManyField(to='restaurants.category'),
        ),
    ]
