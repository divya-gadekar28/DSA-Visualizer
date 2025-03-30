from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

# Login View
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/index")  # Redirect to homepage or dashboard
        else:
            messages.error(request, "Invalid email or password")
            return redirect("/login") 

    return render(request, "login_form.html")

# Logout View
def logout(request):
    auth_logout(request)
    return redirect("/login")

