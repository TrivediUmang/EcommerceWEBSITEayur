from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Cart
from products.models import Product


# -----------------------------
# Add Product To Cart
# -----------------------------

@login_required(login_url="login")
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart_item = Cart.objects.filter(
        user=request.user,
        product=product
    ).first()

    if cart_item:

        cart_item.quantity += 1
        cart_item.save()

    else:

        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )

    return redirect("cart")


# -----------------------------
# Cart Page
# -----------------------------

@login_required(login_url="login")
def cart_page(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    context = {
        "cart_items": cart_items,
        "total": total
    }

    return render(request, "cart.html", context)


# -----------------------------
# Remove Product
# -----------------------------

@login_required(login_url="login")
def remove_from_cart(request, cart_id):

    item = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    item.delete()

    return redirect("cart")