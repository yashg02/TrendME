from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'business/index.html')

def signup(request):
    return render(request, 'business/signup.html')

def login(request):
    return render(request, 'business/login.html')