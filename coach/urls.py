from django.urls import *
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("signup", views.signup_view, name="signup"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("coachadmin", views.coachadmin_view, name="coachadmin"),
    path("teamcoachadmin", views.teamcoachadmin_view, name="teamcoachadmin"),
    path("userPrivateTplan", views.userPrivateTplan_view, name="userPrivateTplan"),
    path("userTeamTplan", views.userTeamTplan_view, name="userTeamTplan"),
    path("schedule", views.schedule_view, name="schedule"),
    path("announcements", views.announcements_view, name="announcements"),
    path("checkout", views.checkout, name="checkout_page"),
    path("payment_form", views.payment_form, name="payment_form")
]
