from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .forms import SignUpForm
from .models import User
def home(req):
    return render(req,'accounts/home.html')



def register(req):
    if req.method=="POST":
        form = SignUpForm(req.POST)

        if form.is_valid():
            data = form.cleaned_data
            firstname = data['FirstName']
            lastname = data['LastName']
            email = data['Email']
            passwd = data['Password']

            user = User.objects.create(full_name=firstname+" "+lastname,email=email,password=passwd)
            user.save()
            username = User.objects.filter(email=email).first().full_name
            messages.success(req,f'Account created for {username}')
            return redirect(reverse('account_login'))
        


    else:
        form = SignUpForm()
    
    return render(req,'accounts/register.html',{"form":form})


def login(req):
    return render(req,'accounts/login.html')