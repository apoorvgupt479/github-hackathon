from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")
def hero(request):
    data = {
        'title': 'Hero Page'
    }
    return render(request, 'hero.html', data)
def aboutus(request):
    return render(request, 'about-us.html')


@login_required(login_url='login')
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

        if not all([username, fname, lname, email, pass1, pass2]):
            messages.error(request, "All fields are required.")
            return redirect('signup')
        if pass1 != pass2:
            return HttpResponse("Different Passwords")
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            messages.success(request, "Your account was created sucessfully.")
            return redirect('login')
    data = {
        'title' : 'Sign up'
    }

    return render(request, 'auth/signup.html', data)

    
def login_view(request):
    data = {
        'title' : 'Log in'
    }
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        # fname = request.POST['fname']
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('hero')
    return render(request, 'auth/signin.html', data)


def logout_page(request):
    logout(request)
    return redirect('login')

def tictactoe(request):
    return render(request, 'games/tictactoe.html')
def memory(request):
    return render(request, 'games/memory.html')

def datahandling(request):
    return render(request, 'quiz/Datahandling.html')
def fractionsdecimals(request):
    return render(request, 'quiz/Fractions&decimals.html')
def heat(request):
    return render(request, 'quiz/Heat.html')
def integers(request):
    return render(request, 'quiz/Integers.html')
def lineangles(request):
    return render(request, 'quiz/Line&angles.html')
def nutritioninanimals(request):
    return render(request, 'quiz/NutritioninAnimals.html')
def simpleequations(request):
    return render(request, 'quiz/SimpleEquations.html')
def nutritioninplants(request):
    return render(request, 'quiz/NutritioninPlants.html')
def fibretofabric(request):
    return render(request, 'quiz/FibretoFabric.html')
def acidsbasessalts(request):
    return render(request, 'quiz/AcidsBasesSalts.html')
