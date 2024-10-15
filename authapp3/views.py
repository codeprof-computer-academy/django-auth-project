from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# home Page
def homePage(request):

    return render(request, 'authapp3/index.html')
    


# register
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    context = {
        "registerform":form
    }
        
    return render(request, 'authapp3/signup.html', context)


# login
def loginPage(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("email")

            user = authenticate(request, username = username, password = password)

            if user is not None:
            
                login(user)
                return redirect("dashboard")

    return render(request, "authapp3/login.html",  {"loginform": form})
        

            


# dashboard
@login_required(login_url="login")
def dashboard(request):
    return render(request, 'authapp3/dashboard.html')