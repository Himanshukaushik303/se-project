from django.shortcuts import render, redirect
from .models import Product, Shop, User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .choices import USER_TYPE_CHOICES

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "api/home.html", context={})
    else:
        return redirect("/login")


def base(request):
    return render(request, "api/base.html", context={})

def cats(request):
    cats = Product.objects.all()
    return render(request,"api/cats.html",context={"cats":cats})

def sellers(request):
    return render(request,"api/sellers.html",context={})


def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        role = request.POST.get("role")
        if role == "buyer":
            role = 3
        else:
            role = 4
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=fname,
            last_name=lname,
            user_type=role,
            phone=phone,
        )
        user.save()
        return redirect("/login")
    return render(request, "api/signup.html", context={})


def view_login(request):
    if request.method == "POST":
        print("login")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # check if user has entered correct credentials
        print(email)
        print(password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("hogya")
            # A backend authenticated the credentials
            return redirect("/")
        else:
            return render(request, "api/login.html")
        # No backend authenticated the credentials
    return render(request, "api/login.html")


def logoutUser(request):
    logout(request)
    return redirect("/login")
