from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    bonus_balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="dishes/")

    def __str__(self):
        return self.name