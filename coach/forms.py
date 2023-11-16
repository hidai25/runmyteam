from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tplan, TeamTplan
from django import forms


class UserForm(UserCreationForm):
    ''' Regsitration form'''
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    member_type = forms.ChoiceField(choices=(('regular', 'regular'), ('premium', 'premium'),
                                             ('coaches', 'coaches')), help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class TplanForm(forms.ModelForm):
    ''' This form builds all the options for the coach to write a training plan'''
    def get_all_users():
        # Get all the users for the form so that the coach can write a plan to premium members
        all_users = User.objects.filter(is_superuser=False, profile__member_type='premium').values('id', 'first_name', 'last_name')
        return [(u['id'], u['first_name'] + ' ' + u['last_name']) for u in all_users]

    Athletes_name = forms.ChoiceField(choices=get_all_users())
    # Facilitates the coaches work by already having selecto options
    objective = forms.ChoiceField(choices=(('leisure', 'leisure'), ('5k', '5k'), ('10k', '10k'),
                                           ('half-marathon', 'half-marathon'), ('marathon', 'marathon')))

    class Meta:
        model = Tplan
        fields = ('Athletes_name', 'objective', 'week_start_date', 'monday_practice', 'tuesday_practice',
                  'wednesday_practice', 'thursday_practice', 'friday_practice', 'saturday_practice', 'sunday_practice', )


class TTeamplanForm(forms.ModelForm):
    ''' This form builds all the options for the coach to write a team trainign plan'''
    objective = forms.ChoiceField(choices=(('Season Start', 'Season Start'), ('Mid Season',
                                                                              'Mid Season'), ('End of the Season', 'End of the Season')))

    class Meta:
        model = TeamTplan
        fields = ('objective', 'week_start_date', 'monday_practice', 'tuesday_practice', 'wednesday_practice',
                  'thursday_practice', 'friday_practice', 'saturday_practice', 'sunday_practice', )
