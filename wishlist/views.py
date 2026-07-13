from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Wishlist


@login_required(login_url="login")
def wishlist(request):

    items = Wishlist.objects.filter(user=request.user)

    return render(
        request,
        "wishlist.html",
        {
            "items": items
        }
    )


@login_required(login_url="login")
def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect("product_detail", product_id=product.id)


@login_required(login_url="login")
def remove_from_wishlist(request, item_id):

    item = get_object_or_404(
        Wishlist,
        id=item_id,
        user=request.user
    )

    item.delete()

    return redirect("wishlist")