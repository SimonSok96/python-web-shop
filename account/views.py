from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.utils.translation import gettext as _
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (_("You have succsessfully loged in")))
            return redirect("shop:product_list")
        else:
            messages.success(request, (_("Wrong password or username")))
            return redirect("login")
    else:
        return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, (_("You have succsessfully loged out")))
    return redirect("shop:product_list")
    
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"] 
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, (_("You have sucsessfuly sing in")))
            return redirect("shop:product_list")
    return render(request, 'register.html', {'form': form})