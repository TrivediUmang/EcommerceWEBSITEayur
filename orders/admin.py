from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "quantity", "total_price", "status", "ordered_at")
    list_filter = ("status", "ordered_at")
    search_fields = ("user__username", "product__name")