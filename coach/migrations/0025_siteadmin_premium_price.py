# Generated by Django 2.0.3 on 2018-05-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0024_auto_20180506_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteadmin',
            name='premium_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
