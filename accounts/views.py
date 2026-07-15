from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Address


@login_required(login_url="login")
def profile(request):

    return render(request, "accounts/profile.html")


@login_required(login_url="login")
def saved_addresses(request):

    addresses = request.user.addresses.all()

    return render(
        request,
        "accounts/addresses.html",
        {
            "addresses": addresses
        }
    )


@login_required(login_url="login")
def add_address(request):

    if request.method == "POST":

        Address.objects.create(

            user=request.user,

            full_name=request.POST.get("full_name"),

            phone=request.POST.get("phone"),

            house=request.POST.get("house"),

            area=request.POST.get("area"),

            city=request.POST.get("city"),

            state=request.POST.get("state"),

            pincode=request.POST.get("pincode"),

        )

        return redirect("saved_addresses")

    return render(request, "accounts/add_address.html")


@login_required(login_url="login")
def settings_view(request):

    return render(
        request,
        "accounts/settings.html"
    )