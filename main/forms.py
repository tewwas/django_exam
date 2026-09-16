from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Client, Dish


class OrderForm(forms.Form):
    dish = forms.ModelChoiceField(
        queryset=Dish.objects.all(),
        label="Блюдо",
    )

    use_bonuses = forms.BooleanField(
        required=False,
        label="Списать бонусы",
    )


class ClientCreationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )