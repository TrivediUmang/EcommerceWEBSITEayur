from django.urls import path
from . import views

urlpatterns = [

    # Dashboard
    path(
        "",
        views.profile,
        name="profile"
    ),

    # Saved Addresses
    path(
        "addresses/",
        views.saved_addresses,
        name="saved_addresses"
    ),

    # Add Address
    path(
        "addresses/add/",
        views.add_address,
        name="add_address"
    ),

]