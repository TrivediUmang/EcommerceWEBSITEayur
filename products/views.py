from django.shortcuts import render
from .models import Product, Category , Blog, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

def home(request):

    # Sirf 4 Featured Products
    products = Product.objects.all()[:3]

    categories = Category.objects.all()

    context = {
        "products": products,
        "categories": categories
    }

    return render(request, "home.html", context)


def shop(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    # Category Filter
    category_slug = request.GET.get("category")

    if category_slug:
        products = products.filter(category__slug=category_slug)

    # Search
    search = request.GET.get("search")

    if search:
        products = products.filter(name__icontains=search)

    # Sorting
    sort = request.GET.get("sort")

    if sort == "low":
        products = products.order_by("price")

    elif sort == "high":
        products = products.order_by("-price")

    elif sort == "name":
        products = products.order_by("name")

    context = {
        "products": products,
        "categories": categories
    }

    return render(request, "shop.html", context)

def about(request):
    return render(request, "about.html")

from .models import Product, Category, Blog
def blogs(request):

    blogs = Blog.objects.all()

    return render(request, "blogs.html", {
        "blogs": blogs
    })

def blogs(request):

    blogs = Blog.objects.all()

    context = {
        "blogs": blogs
    }

    return render(request, "blogs.html", context)

def contact(request):

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")
        )

    return render(request, "contact.html")


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")

def register(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Password Match Check
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Username Exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        # Email Exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        # Create User
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, "register.html")
    