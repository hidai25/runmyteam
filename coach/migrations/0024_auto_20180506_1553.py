# Generated by Django 2.0.3 on 2018-05-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0023_auto_20180505_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaches',
            name='coach_image',
            field=models.ImageField(blank=True, null=True, upload_to='stuff_image'),
        ),
    ]
