from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from seller.models import NetworkNode, Product, Supplier


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'data',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('country', 'city',)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts_email', 'contacts_country', 'product', 'supplier_link', 'debt_to_supplier', 'created_at')
    list_filter = ('contacts_country', 'contacts_city',)
    actions = ['clear_debt']

    def supplier_link(self, obj):
        return obj.supplier.name if obj.supplier else '-'

    supplier_link.short_description = 'Поставщик'

    def debt_to_supplier(self, obj):
        return f"{obj.debt_to_supplier:.2f}" if obj.debt_to_supplier else '-'

    debt_to_supplier.short_description = 'Задолженность перед поставщиком'

    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0)

    clear_debt.short_description = _('Очистить задолженность')


