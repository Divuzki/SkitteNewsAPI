from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Function based views to Class Based Views

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request, *args, **kwargs):
    return render(request, "index.html")


def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    next_url = request.GET.get("next") or None
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        return redirect("/")
    elif request.user.is_authenticated:
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Login",
        "title": "Login"
    }
    return render(request, "auth.html", context)


def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    elif not request.user.is_authenticated:
        return redirect("/login")
    context = {
        "form": None,
        "description": "Are you sure you want to logout?",
        "btn_label": "Click to Confirm",
        "title": "Logout"
    }
    return render(request, "auth.html", context)


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=True)
            user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, user)
            return redirect("/docs")
        elif request.user.is_authenticated:
            return redirect("/")
    context = {
        "form": form,
        "btn_label": "Register",
        "title": "Register"
    }
    return render(request, "auth.html", context)


def admin_view(request, *args, **kwargs):
    qt = request.GET.get("whoami")
    if qt == "amowner":
      return redirect("/admin121234admin2345678admin2345678")
