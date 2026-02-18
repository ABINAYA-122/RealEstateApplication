from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def register(request):
    return HttpResponse("Register Page Working")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("Login Successful")
        else:
            return HttpResponse("Invalid Username or Password")

    return render(request, "login.html")