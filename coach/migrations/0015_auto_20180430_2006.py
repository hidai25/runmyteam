# Generated by Django 2.0.3 on 2018-04-30 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0014_auto_20180430_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tplan',
            old_name='prep_for',
            new_name='objective',
        ),
    ]