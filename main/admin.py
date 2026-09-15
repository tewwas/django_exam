from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Client, Dish


@admin.register(Client)
class ClientAdmin(UserAdmin):
    pass


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price")