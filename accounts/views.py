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