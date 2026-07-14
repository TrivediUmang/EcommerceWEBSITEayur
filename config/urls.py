"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Admin
    path("admin/", admin.site.urls),

    # Django Allauth
    path("accounts/", include("allauth.urls")),

    # Products (Home, Shop, About, Contact, Blogs)
    path("", include("products.urls")),

    # Cart
    path("cart/", include("cart.urls")),

    # User Dashboard
    path("account/", include("accounts.urls")),

    # Orders
    path("orders/", include("orders.urls")),

    path("wishlist/", include("wishlist.urls")),

    path("account/", include("accounts.urls")),

]

# Serve Media & Static Files (Development)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)