from django import forms

class SignUpForm(forms.Form):
    FirstName = forms.CharField(max_length=50,required=True)
    LastName = forms.CharField(max_length=50,required=True)
    Email = forms.EmailField(required=True)

    Password = forms.CharField(widget=forms.PasswordInput(),min_length=5,max_length=15)
    PasswordConfirm = forms.CharField(widget=forms.PasswordInput(),min_length=5,max_length=15)

class LoginForm(forms.Form):
    Email = forms.EmailField(required=True)
    Password = forms.CharField(widget=forms.PasswordInput(),min_length=5,max_length=15)