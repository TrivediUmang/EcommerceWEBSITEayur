from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("shop/", views.shop, name="shop"),

    path("about/", views.about, name="about"),

    path("blogs/", views.blogs, name="blogs"),

    path("contact/", views.contact, name="contact"),

    path("login/", views.user_login, name="login"),

    path(
        "logout/",
        LogoutView.as_view(next_page="home"),
        name="logout"
    ),

    path("register/", views.register, name="register"),

    path(
        "add-to-cart/<int:product_id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    path(
       "product/<int:product_id>/",
       views.product_detail,
       name="product_detail"
),
]