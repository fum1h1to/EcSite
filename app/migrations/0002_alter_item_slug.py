# Generated by Django 4.0.5 on 2022-06-25 11:55

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=app.models.slug_maker, max_length=64, unique=True),
        ),
    ]