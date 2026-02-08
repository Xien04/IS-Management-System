from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, RegisterForm
from .models import Profile


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboad:index")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect("accounts:profile")
    else:
        form = RegisterForm()
    
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile(request):
    profile_obj, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile_obj)
        if form.is_valid():
            messages.success(request, "Profile Update")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=profile_obj)

    return render(request, "accounts/profile.html", {"form": form})
    
