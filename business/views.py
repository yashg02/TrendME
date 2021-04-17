from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Dashboard

# Create your views here.
def index(request):
    return render(request, 'business/index.html')

def signup(request):
    return render(request, 'business/signup.html')

def login(request):
    return render(request, 'business/login.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if User.objects.filter(username=username).exists():
            messages.error(request, " Company already exists")
            return redirect('signup')


        if len(username)>20:
            messages.error(request, " Your Company name must be under 20 characters")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('signup')
            
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('signup')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        # messages.success(request, " Your account has been successfully created")
        auth_login(request, myuser)
        return redirect('Homepage')

    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            auth_login(request, user)
            return redirect("Homepage",)
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")

    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')

def search(request):
    query=request.GET['query']
    allPosts= Dashboard.objects.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request, 'business/search.html', params)

def trending(request):
    alloffer = Dashboard.objects.all()
    return render(request,'business/trending.html',{'offer':alloffer})

@login_required
def dashboard(request):
        return render(request,'business/addOffers.html')

@login_required
def handleoffer(request):
    if request.method=="POST":
        usr = request.user
        name = request.POST.get('title', '')
        desc=request.POST.get('desc', '')
        img = request.POST.get('image', '')
        price = request.POST.get('price', '')
        dprice = request.POST.get('dprice', '')

        profile = Dashboard(user=usr,title=name, description=desc, img=img, price=price, dprice=dprice)
        profile.save()

    return redirect("dashboard")

@login_required
def manage(request):
    totaloffer = Dashboard.objects.filter(user=request.user)
    print(totaloffer)
    return render(request,"business/manageOffers.html",{'total':totaloffer})

@login_required
def delete(request,name):
    Dashboard.objects.filter(user=request.user,title=name).delete()
    return redirect('manage')

