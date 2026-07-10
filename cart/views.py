from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem


@login_required(login_url="login")
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


@login_required(login_url="login")
def cart_view(request):

    cart, created = Cart.objects.get_or_create(user=request.user)

    items = cart.items.all()

    total = sum(item.total_price for item in items)

    context = {
        "cart": cart,
        "items": items,
        "total": total,
    }

    return render(request, "cart.html", context)

@login_required(login_url="login")
def increase_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect("cart")


@login_required(login_url="login")
def decrease_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if item.quantity > 1:

        item.quantity -= 1

        item.save()

    else:

        item.delete()

    return redirect("cart")


@login_required(login_url="login")
def remove_from_cart(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.delete()

    return redirect("cart")