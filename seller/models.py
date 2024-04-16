from django.db import models
from config import settings
from users.models import User


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(verbose_name='Модель', max_length=100)
    data = models.DateField(verbose_name='Дата_выхода')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    email = models.EmailField(verbose_name="email")
    country = models.CharField(max_length=100, verbose_name="страна")
    city = models.CharField(max_length=100, verbose_name="город")
    street = models.CharField(max_length=100, verbose_name="улица")
    house_number = models.CharField(max_length=10, verbose_name="номер дома")

    def __str__(self):
        return self.name, self.email

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class NetworkNode(models.Model):
    FACTORY = 0
    RETAILER = 1
    INDIVIDUAL = 2
    NODE_CHOICES = [
        (FACTORY, 'Factory'),
        (RETAILER, 'Retailer'),
        (INDIVIDUAL, 'Individual')
    ]
    node_type = models.IntegerField(choices=NODE_CHOICES)
    name = models.CharField(max_length=100, verbose_name="название")
    contacts_email = models.EmailField(verbose_name="email")
    contacts_country = models.CharField(max_length=100, verbose_name="страна")
    contacts_city = models.CharField(max_length=100, verbose_name="город")
    contacts_street = models.CharField(max_length=100, verbose_name="улица")
    contacts_house_number = models.CharField(max_length=10, verbose_name="номер дома")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Продукт')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True, verbose_name="поставщик")
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="задолженность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="время создания ")

    def str(self):
        return self.name

    class Meta:
        verbose_name = "звено сети"
        verbose_name_plural = "звенья сети"

