from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import UserForm, TplanForm, TTeamplanForm
from django.contrib.auth.models import User, Group
from .models import Tplan, SiteAdmin, Coaches, Profile, TeamTplan
from django.conf import settings
import datetime
import stripe


def index(request):
    ''' home page '''
    # Show all the information when loading home page
    context = {
        "user": request.user,
        "team_details": SiteAdmin.objects.filter(),
        "coach_image": Coaches.objects.filter()[:4],
    }
    if not request.user.is_authenticated:
        return render(request, "coach/index.html", context)
    return render(request, "coach/index.html", context)


def login_view(request):
    ''' Handles users login '''
    if request.method == 'GET':
        return render(request, "coach/login.html")
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Make sure a user who signed up and didn't pay doesn't login and conside ther other possibilites
            if user.profile.member_type != 'premium' or user.profile.charge_id is not None:
                login(request, user)
            else:
                # Put user id in session and redirect to payment form
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse("payment_form"))
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "coach/login.html", {"message": "invalid credentials"})


def logout_view(request):
    ''' Handles users logout '''
    logout(request)
    return redirect('index')


def signup_view(request):
    ''' Handles users signup '''
    # Taken from django documentation.
    if request.method == 'GET':
        form = UserForm()
        return render(request, "coach/signup.html", {'form': form})
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            member_type = form.cleaned_data.get('member_type')
            group = Group.objects.filter(name=member_type)
            user.groups.add(group[0])
            user.profile.member_type = member_type
            user.save()
            if request.POST['member_type'] == "premium":
                request.session['user_id'] = user.id
                return redirect('payment_form')
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserForm()
    return render(request, 'coach/signup.html', {'form': form})


def coachadmin_view(request):
    ''' Function responsible for the coache's office feature where he makes private plans for premium users'''
    form = TplanForm()
    form1 = TTeamplanForm()

    if request.method == 'GET':
        return render(request, 'coach/admin.html', {'form': form, 'form1': form1})
    if request.method == 'POST':
        form = TplanForm(request.POST)
        if form.is_valid():
            # Get the profile of the current athelete plan
            prof = User.objects.get(pk=request.POST['Athletes_name'])
            plan = form.save(commit=False)
            # Relate the plan to the athlete
            plan.profile = prof.profile
            plan.save()
            form = TplanForm()
    return render(request, 'coach/admin.html', {'form': form, 'form1': form1, "message": "Private Pratice Submitted"})


def teamcoachadmin_view(request):
    ''' Function responsible to post team plans by the coach '''
    if request.method == 'POST':
        form1 = TTeamplanForm(request.POST)
        form = TplanForm()
        if form1.is_valid():
            form1.save()
            form1 = TTeamplanForm()

    return render(request, 'coach/admin.html', {'form': form, 'form1': form1, "message1": "Team Practice Submitted"})


def userPrivateTplan_view(request):
    ''' Function reponsible for showing private plans'''
    prof = Profile.objects.get(user=request.user)
    context = {
        # The filter makes sure that the athlete sees the plan for one month only
        "Athletes_name": Tplan.objects.filter(profile=prof, week_start_date__gt=datetime.datetime.now() - datetime.timedelta(days=30))
    }
    return render(request, 'coach/userPrivateTplan.html', context)


def userTeamTplan_view(request):
    ''' This function is responsible for showing the team training plans'''
    context = {
        "team_plan": TeamTplan.objects.filter(week_start_date__gt=datetime.datetime.now() - datetime.timedelta(days=30))
    }
    return render(request, 'coach/userTeamTplan.html', context)


def schedule_view(request):
    '''This function is responsible for showing the google calendar'''
    context = {
    }
    if request.method == 'GET':
        return render(request, 'coach/schedule.html', context)


def announcements_view(request):
    ''' This function is responsible for showing the announcments made by the admin(pinax announcments)'''
    context = {
    }
    if request.method == 'GET':
        return render(request, 'coach/announcements.html', context)


def payment_form(request):
    ''' This function is responsible for showing the payment form in which there is a link to stripe payments clearing.'''
    context = {"stripe_key": settings.STRIPE_PUBLIC_KEY,
               "team_name": SiteAdmin.objects.filter(),
               }

    return render(request, "coach/payment_form.html", context)


stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    ''' Function responsible to process the payment and redirect the user after that '''
    user = Profile.objects.get(user__id=request.session['user_id'])
    user.member_type = "premium"

    if request.method == "POST":
        token = request.POST.get("stripeToken")

    try:
        charge = stripe.Charge.create(
            # Amount is in cents
            amount=2000,
            currency="usd",
            source=token,
            description="The product charged to the user"
        )

        user.charge_id = charge.id

    except stripe.error.CardError as ce:
        return False, ce

    else:
        user.save()
        # Update new user 
        request.session.modified = True
        login(request, user)
        return render(request, "coach/login.html", {"message": "Thank you! Please login with your Credentials!"})
