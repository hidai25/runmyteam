# Generated by Django 2.0.3 on 2018-05-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0021_auto_20180504_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_login',
            field=models.CharField(blank=True, max_length=234, null=True),
        ),
    ]
