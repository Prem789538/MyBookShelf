from django.shortcuts import render,redirect
from django.urls import reverse
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
            return redirect(reverse('account login'))
        else:
            return render(req,'accounts/register.html',{'form':form})


    else:
        form = SignUpForm()
        return render(req,'accounts/register.html',{"form":form})


def login(req):
    return render(req,'accounts/login.html')