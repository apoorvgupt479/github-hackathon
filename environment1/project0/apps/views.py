from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")
def hero(request):
    data = {
        'title': 'Hero Page'
    }
    return render(request, 'hero.html', data)
def home(request):
    data = {
        'title': 'Home Page',
        'uname': 'aditya',
    }
    return render(request, 'home.html', data)

def aboutus(request):
    data = {
        'title': 'About us'
    }
    return render(request, 'about-us.html', data)

        
def signup(request):
    if request.method == 'POST':    
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            return HttpResponse("Different Passwords")
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            messages.success(request, "Your account was created sucessfully.")
            return redirect('signin')
    data = {
        'title' : 'Sign up'
    }

    return render(request, 'auth/signup.html', data)

    
def signin(request):
    data = {
        'title' : 'Sign in'
    }
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        # fname = request.POST['fname']
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('hero')
    return render(request, 'auth/signin.html', data)


def signout(request):

    logout(request)
    return redirect('login')