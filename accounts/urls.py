from django.urls import path
from . import views

urlpatterns = [

    # Dashboard
    path("", views.profile, name="profile"),

    # Saved Address
    path(
        "addresses/",
        views.saved_addresses,
        name="saved_addresses"
    ),

]