# Generated by Django 2.0.3 on 2018-04-29 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0008_remove_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tplan',
            name='practice_description',
        ),
    ]