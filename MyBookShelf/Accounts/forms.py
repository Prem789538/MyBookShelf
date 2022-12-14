from django import forms
from django.core.exceptions import ValidationError
from .models import User

def email_validator_sigup(email_form):
    user = User.objects.filter(email=email_form)
    if user:
        raise ValidationError(f'Email already exists!')
    else:
        return email_form

class SignUpForm(forms.Form):
    FirstName = forms.CharField(max_length=50,required=True)
    LastName = forms.CharField(max_length=50,required=True)
    Email = forms.EmailField(required=True,validators=[email_validator_sigup])

    Password = forms.CharField(widget=forms.PasswordInput(),min_length=5,max_length=15)
    PasswordConfirm = forms.CharField(widget=forms.PasswordInput(),min_length=5,max_length=15)



class LoginForm(forms.Form):
    Email = forms.EmailField(required=True)
    Password = forms.CharField(widget=forms.PasswordInput(),min_length=5,max_length=15)