from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    ''' Info about the user's profile'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_type = models.CharField(max_length=30, blank=True)
    charge_id = models.CharField(max_length=234, null=True, blank=True)
    last_login = models.DateTimeField(max_length=234, null=True, blank=True)

    class Meta:
        # Creates custom permissions in django
        permissions = (
            ("see_private_plan", "Can see private plan"),
            ("see_coach_access", "Can see coach access"),
        )

    def __str__(self):
        return f"{self.user} {self.member_type} {self.last_login}"


# Save user to profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Update users in profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Tplan(models.Model):
    ''' Info about the user's premium private Training plan'''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    objective = models.CharField(max_length=200, blank=True)
    week_start_date = models.DateField(max_length=200, blank=False)
    Athletes_name = models.CharField(max_length=30, blank=False)
    monday_practice = models.CharField(max_length=200, blank=False)
    tuesday_practice = models.CharField(max_length=200, blank=False)
    wednesday_practice = models.CharField(max_length=200, blank=False)
    thursday_practice = models.CharField(max_length=200, blank=False)
    friday_practice = models.CharField(max_length=200, blank=False)
    saturday_practice = models.CharField(max_length=200, blank=False)
    sunday_practice = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.Athletes_name} {self.week_start_date} {self.objective}"


class TeamTplan(models.Model):
    ''' Info about the team Training plan'''
    objective = models.CharField(max_length=200, blank=True)
    week_start_date = models.DateField(max_length=200, blank=False)
    monday_practice = models.CharField(max_length=200, blank=False)
    tuesday_practice = models.CharField(max_length=200, blank=False)
    wednesday_practice = models.CharField(max_length=200, blank=False)
    thursday_practice = models.CharField(max_length=200, blank=False)
    friday_practice = models.CharField(max_length=200, blank=False)
    saturday_practice = models.CharField(max_length=200, blank=False)
    sunday_practice = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.objective} {self.week_start_date}"


class SiteAdmin(models.Model):
    ''' Info about the team who bought this app and uses it'''
    team_name = models.CharField(max_length=64, blank=True)
    athlete_number = models.IntegerField(default=0)
    about_the_team = models.CharField(max_length=200, blank=True)
    stuff_image = models.ImageField(upload_to='stuff_image', blank=True)
    premium_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    email_field =models.EmailField(null=True)

    def __str__(self):
        return f"{self.team_name} {self.athlete_number}"


class Coaches(models.Model):
    ''' Info about the team's coaches'''
    coach_name = models.CharField(max_length=64, blank=True)
    coach_image = models.ImageField(upload_to='stuff_image', blank=True, null=True)

    def __str__(self):
        return f"{self.coach_name}"
