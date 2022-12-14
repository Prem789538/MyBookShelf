from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from .forms import SignUpForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import auth

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
            #passwd = make_password(data['Password'])
            passwd = data['Password']
            user = User.objects.create_user(username=firstname+" "+lastname,email=email,password=passwd)
            user.save()
            auth.login(req,user)
            
            
            return redirect(reverse('account_login'))
        


    else:
        form = SignUpForm()
    
    return render(req,'accounts/register.html',{"form":form})


def login(req):
    if req.method=="POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            passwd = form.cleaned_data['Password']

            user = auth.authenticate(req,username=email,password=passwd)
            if user:
                auth.login(req,user)
                messages.success(req,'Login Successful')

                return redirect(reverse('account_home'))
            else:
                messages.warning(req,'Login failed!')

    else:
        form = LoginForm()
    
    return render(req,'accounts/login.html',{'form':form})



def logout(req):
    return render(req,"accounts/logout.html")

