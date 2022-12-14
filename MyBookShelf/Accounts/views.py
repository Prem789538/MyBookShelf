from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from .forms import SignUpForm,LoginForm
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
            #passwd = make_password(data['Password'])
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
    if req.method=="POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            passwd = form.cleaned_data['Password']

            user = User.objects.filter(email=email).first()
            if user and user.password == passwd:
                messages.success(req,'Login Successful')

                return redirect(reverse('account_home'))
            else:
                messages.warning(req,'Login failed!')


                



    else:
        form = LoginForm()
    
    return render(req,'accounts/login.html',{'form':form})