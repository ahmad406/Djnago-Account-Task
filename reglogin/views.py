from django.contrib import auth
from django.contrib.auth import authenticate,login,logout as auth_logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.shortcuts import redirect, render
from .form import *

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random


# Create your views here.
def index(request):
    return render(request,'index.html')

#User Registration
def register(request):
    if request.method == 'POST':
        fm  = SignUpForm(request.POST , request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    else:
        fm = SignUpForm()
    return render(request,'register.html', {'form':fm},)


#User login
def login(request):
    if request.method == "POST":
        fm=LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname= fm.cleaned_data['username']
            upass= fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('/profile')
    else:
     fm=LoginForm()
    return render(request,'login.html', {'form':fm})


#user Profile
def profile(request):
    if request.method == "POST":
        formp = ProfileP(request.POST, request.FILES,instance=request.user.profile)
        if formp.is_valid():
            formp.save()
            return redirect('profile')
    else:
        formp = ProfileP()
    return render(request,'profile.html',{'formp':formp})

#userlogout
def logout(request):
    auth_logout(request)
    return redirect('/login')

#update user
def Upadate(request,id):
    if request.method == 'POST':
       pi = User.objects.get(pk=id)
       fm = UpdateProfile(request.POST, instance=pi)
       if fm.is_valid():
        fm.save()
        return render(request,'profile.html')
    else:
        pi = User.objects.get(pk=id)
        fm = UpdateProfile( instance=pi)
    return render(request,'update.html' ,{'form':fm})


#Delete user
def Delete(request, id):

    user = User.objects.get(id=id)  
    user.delete()  
    return redirect("/register")


#otp varification
# def home(request):
#      return render(request, "home.html")

# def generateOTP() :
#      digits = "0123456789"
#      OTP = ""
#      for i in range(4) :
#          OTP += digits[math.floor(random.random() * 10)]
#      return OTP

# def send_otp(request):
#      email=request.GET.get   ("email")
#      print(email)
#      o=generateOTP()
#      htmlgen = '<p>Your OTP is <strong>o</strong></p>'
#      send_mail('OTP request',o,'<ahmadsayyed66@gmail.com>',[email], fail_silently=False, html_message=htmlgen)
#      print(o)
#      return HttpResponse(o)
def changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm  = SetPass(request.POST , data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return redirect('login')
        else:
            fm = SetPass(user=request.user)
        return render(request,'changepassword.html',{'form':fm})
    else:
        return render(request,'profile.html')

