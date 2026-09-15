from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Client, Dish, Order


@admin.register(Client)
class ClientAdmin(UserAdmin):
    pass


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("client", "dish", "created_at")
    list_filter = ("created_at",)