# Generated by Django 2.0.3 on 2018-04-28 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_type', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='stuff_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SiteAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=64)),
                ('athlete_number', models.IntegerField(default=0)),
                ('about_the_team', models.CharField(blank=True, max_length=200)),
                ('stuff_image', models.ImageField(blank=True, upload_to='stuff_image')),
            ],
        ),
        migrations.CreateModel(
            name='Tplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_description', models.CharField(blank=True, max_length=200)),
                ('prep_for', models.CharField(blank=True, max_length=200)),
                ('start_date', models.DateField(blank=True, max_length=200)),
                ('Athletes_name', models.CharField(blank=True, max_length=30)),
                ('practice_day', models.CharField(blank=True, max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.Profile')),
            ],
        ),
    ]