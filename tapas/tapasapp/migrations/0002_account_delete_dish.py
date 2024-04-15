# Generated by Django 5.0.3 on 2024-04-07 03:02

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapasapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
    ]
