from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from BarchuckBank.models import Transfer


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = (
            'recipient_name',
            'recipient_account',
            'title',
            'amount',
        )


class SQLInjectionForm(forms.Form):
    title = forms.CharField(max_length=1000)


class AdminTransferConfirmation(forms.Form):
    confirmed = forms.BooleanField()
