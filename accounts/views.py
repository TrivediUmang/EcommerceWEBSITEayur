from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="login")
def profile(request):
    return render(request, "accounts/profile.html")

    from django.contrib.auth.decorators import login_required

@login_required
def saved_addresses(request):

    addresses = request.user.addresses.all()

    return render(
        request,
        "accounts/addresses.html",
        {
            "addresses": addresses
        }
    )

    from .models import Address

@login_required
def add_address(request):

    if request.method == "POST":

        Address.objects.create(
            user=request.user,
            full_name=request.POST["full_name"],
            phone=request.POST["phone"],
            house=request.POST["house"],
            area=request.POST["area"],
            city=request.POST["city"],
            state=request.POST["state"],
            pincode=request.POST["pincode"],
        )

        return redirect("saved_addresses")

    return render(request, "accounts/add_address.html")