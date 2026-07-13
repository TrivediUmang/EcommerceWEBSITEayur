from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Product, Category, Blog, Contact


# ===========================
# HOME
# ===========================

def home(request):

    return render(request, "home.html")


# ===========================
# SHOP
# ===========================

def shop(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    category_slug = request.GET.get("category")

    if category_slug:
        products = products.filter(category__slug=category_slug)

    search = request.GET.get("search")

    if search:
        products = products.filter(name__icontains=search)

    sort = request.GET.get("sort")

    if sort == "low":
        products = products.order_by("price")

    elif sort == "high":
        products = products.order_by("-price")

    elif sort == "name":
        products = products.order_by("name")

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "shop.html", context)


# ===========================
# ABOUT
# ===========================

def about(request):

    return render(request, "about.html")


# ===========================
# BLOGS
# ===========================

def blogs(request):

    blogs = Blog.objects.all()

    return render(
        request,
        "blogs.html",
        {
            "blogs": blogs
        }
    )


# ===========================
# CONTACT
# ===========================

def contact(request):

    if request.method == "POST":

        Contact.objects.create(

            name=request.POST.get("name"),

            email=request.POST.get("email"),

            phone=request.POST.get("phone"),

            subject=request.POST.get("subject"),

            message=request.POST.get("message"),

        )

        messages.success(request, "Message Sent Successfully.")

    return render(request, "contact.html")


# ===========================
# LOGIN
# ===========================

def user_login(request):

    if request.user.is_authenticated:

        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(

            request,

            username=username,

            password=password,

        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:

            messages.error(

                request,

                "Invalid Username or Password"

            )

    return render(request, "login.html")


# ===========================
# REGISTER
# ===========================

def register(request):

    if request.user.is_authenticated:

        return redirect("home")

    if request.method == "POST":

        first_name = request.POST.get("first_name")

        last_name = request.POST.get("last_name")

        username = request.POST.get("username")

        email = request.POST.get("email")

        password = request.POST.get("password")

        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("register")

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("register")

        if User.objects.filter(email=email).exists():

            messages.error(
                request,
                "Email already exists."
            )

            return redirect("register")

        User.objects.create_user(

            username=username,

            first_name=first_name,

            last_name=last_name,

            email=email,

            password=password,

        )

        messages.success(

            request,

            "Registration Successful."

        )

        return redirect("login")

    return render(request, "register.html")


# ===========================
# CART
# ===========================

def add_to_cart(request, product_id):

    return redirect("shop")

    # ===========================
# PRODUCT DETAILS
# ===========================

def product_detail(request, product_id):

    product = Product.objects.get(id=product_id)

    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]

    context = {
        "product": product,
        "related_products": related_products,
    }

    return render(
        request,
        "product_detail.html",
        context
    )