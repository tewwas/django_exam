from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClientCreationForm, OrderForm
from .models import Dish, Order


def dishes(request):
    dishes = Dish.objects.all()

    return render(
        request,
        "dishes.html",
        {"dishes": dishes},
    )


@login_required
def create_order(request):
    dish_id = request.GET.get("dish")

    initial = {}

    if dish_id:
        dish = get_object_or_404(Dish, id=dish_id)
        initial["dish"] = dish

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            Order.objects.create(
                client=request.user,
                dish=form.cleaned_data["dish"],
            )

            return redirect("home")
    else:
        form = OrderForm(initial=initial)

    return render(
        request,
        "order_form.html",
        {"form": form},
    )


@login_required
def orders(request):
    orders = Order.objects.filter(
        client=request.user
    ).select_related("dish")

    return render(
        request,
        "orders.html",
        {"orders": orders},
    )


def register(request):
    if request.method == "POST":
        form = ClientCreationForm(request.POST)

        if form.is_valid():
            client = form.save()
            login(request, client)

            return redirect("home")
    else:
        form = ClientCreationForm()

    return render(
        request,
        "register.html",
        {"form": form},
    )


class ClientLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True


def client_logout(request):
    logout(request)
    return redirect("home")