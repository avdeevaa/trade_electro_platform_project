from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    country = models.CharField(max_length=100, verbose_name="страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=200, verbose_name="улица")
    house_number = models.PositiveIntegerField(verbose_name="номер дома")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
