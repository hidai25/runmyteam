# Generated by Django 2.0.3 on 2018-05-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0018_teamtplan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamtplan',
            name='Athletes_name',
        ),
        migrations.RemoveField(
            model_name='teamtplan',
            name='profile',
        ),
    ]
