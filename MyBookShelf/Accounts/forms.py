from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def email_validator_signup(email_form):
    user = User.objects.filter(email=email_form)
    if user:
        raise ValidationError('Email already exists!')
    else:
        return email_form


class SignUpForm(forms.Form):
    FirstName = forms.CharField(max_length=50,required=True)
    LastName = forms.CharField(max_length=50,required=True)
    Email = forms.EmailField(required=True,validators=[email_validator_signup])

    Password = forms.CharField(widget=forms.PasswordInput(),min_length=5,max_length=15)
    PasswordConfirm = forms.CharField(widget=forms.PasswordInput(),min_length=5,max_length=15)

    def clean(self):
        super(SignUpForm,self).clean()

        pwd = self.cleaned_data.get('Password','')
        pwdcnf = self.cleaned_data.get('PasswordConfirm','')
        if pwd != pwdcnf:
            raise ValidationError('Passwords do not match!')



class LoginForm(forms.Form):
    Email = forms.EmailField(required=True)
    Password = forms.CharField(widget=forms.PasswordInput(),min_length=5,max_length=15)