from django.core.checks import messages
from django.db import models
from django.shortcuts import redirect, render 
from django.http import HttpResponse
from django.contrib import messages

from .models import Notes

from django.http import *
#from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
#from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()
#from app.models import Post
# Create your views here.
def home(request):
    return render(request,'app/index.html')
def about(request):
    return render(request,'app/about.html')
def signin(request):
  
        #context = RequestContext(request)
        if request.method == 'POST':
            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
            username = request.POST.get('logid')
            password = request.POST.get('logpassword')
            
            user = authenticate(username=username, password=password)
            
            print("auth",str(authenticate(request, username=username, password=password)))
            print(user,'hi')
        

            if user:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/my_account')
            else:
                messages.error(request, "This username is already taken")
                return redirect("/sign_in")
                

        # else:
        #     # Bad login details were provided. So we can't log the user in.
        #     print ("Invalid login details: {0}, {1}")
        #     return HttpResponse("Invalid login details supplied.")
        # #else:
        #     #return render_to_response('home')
        return render(request,'app/sign_in.html')





def my_account(request):
    if request.user.is_authenticated:
        user = request.user
        
        userdata = User.objects.get(email=user)
        user_name = userdata.name
        user_mobile =  userdata.mobile
        user_email = userdata.email
        user_deg = userdata.deg
        user_degree = userdata.degree
        user_spelazitaon = userdata.spelazitaon
        user_profileimg =userdata.profileimg

        print(user_name , user_profileimg)

        #logout=logout(request)

        # notes=Notes.objects.filter(user=request.user)
        

        
        

        return render(request,'app/my_account.html', locals())
    else:
        return redirect('/sign_in')
    
def logout_view(request):
    logout(request)
    return redirect('/sign_in')
    

def teachers(request):
    return render(request,'app/teachers.html')

def signup(request):
    if request.method=='POST' and request.FILES['profileimg']:
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        deg = request.POST['deg']
        sex = request.POST['sex']
        degree = request.POST['degree']
        spelazitaon = request.POST['spelazitaon']
        about = request.POST['about']
        profileimg = request.FILES['profileimg']
        myuser= User.objects.create_user(username=email, email=email, password=password)
        myuser.email=email
        myuser.mobile=mobile
        myuser.name=name
        myuser.deg=deg
        myuser.sex=sex
        myuser.degree=degree
        myuser.spelazitaon=spelazitaon
        myuser.about=about
        myuser.profileimg=profileimg
        myuser.save()
        return redirect('/sign_in')
    
    return render(request,'app/sign_up.html')
    
def contact(request):
    return render(request,'app/contact.html')



          
         
