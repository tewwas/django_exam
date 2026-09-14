from django.contrib import admin
from django.urls import path
from django.shortcuts import render


def test_page(request):
    return render(request, "test.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", test_page, name="home"),
]