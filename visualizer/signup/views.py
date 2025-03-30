import random

from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

    
# Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        email = request.POST.get("email")
        phone = request.POST.get("phno")
        password = request.POST.get("password")

        # Check if the user already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered !!!")
            return redirect("/signup") 

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password, first_name=username)
        user.save()
        return redirect("/login")

    return render(request, "signup_form.html")
