from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Client


@admin.register(Client)
class ClientAdmin(UserAdmin):
    pass