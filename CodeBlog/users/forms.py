from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from wagtail.users.forms import UserEditForm, UserCreationForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password',)
        
        
class CustomUserEditForm(UserEditForm):
    first_name = forms.CharField(required=True, label=_('First Name'))
    last_name = forms.CharField(required=True, label=_('Last Name'))
    
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, label=_('First Name'))
    last_name = forms.CharField(required=True, label=_('Last Name'))