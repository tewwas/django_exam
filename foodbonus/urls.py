from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main.views import (
    ClientLoginView,
    client_logout,
    create_order,
    dishes,
    orders,
    register,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", dishes, name="home"),

    path("register/", register, name="register"),

    path("login/", ClientLoginView.as_view(), name="login"),

    path("logout/", client_logout, name="logout"),

    path("orders/create/", create_order, name="create_order"),

    path("orders/", orders, name="orders"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )