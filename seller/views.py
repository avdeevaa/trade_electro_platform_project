from django.shortcuts import render
from rest_framework import generics, filters

from seller.models import Supplier, NetworkNode
from seller.permissions import IsActive
from seller.serializers import SupplierSerializer, NetworkNodeSerializer


class SupplierCreateAPIView(generics.CreateAPIView):
    """ Создаем поставщика """
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]


class SupplierListAPIView(generics.ListAPIView):
    """ Просматриваем всех поставщиков и настраиваем фильтр по стране"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [filters.SearchFilter, filters.BaseFilterBackend]
    search_fields = ['country']
    filterset_fields = ['country']
    permission_classes = [IsActive]


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """ Просматриваем одного поставщика """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActive]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """ Редактируем поставщика """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActive]

    def update(self, request, *args, **kwargs):
        """Запрещаем обновление поля задолженность"""
        if 'debt' in request.data:
            del request.data['debt_to_supplier']
        return super().update(request, *args, **kwargs)


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """ Удаляем поставшика """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActive]


class NetworkNodeListAPIView(generics.ListAPIView):
    """ Просматриваем все звенья сети и настраиваем фильтр по стране"""
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    filter_backends = [filters.SearchFilter, filters.BaseFilterBackend]
    search_fields = ['contacts_country']
    filterset_fields = ['contacts_country']
    permission_classes = [IsActive]


class NetworkNodeUpdateAPIView(generics.UpdateAPIView):
    """ Редактируем звенья сети """
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [IsActive]

    def update(self, request, *args, **kwargs):
        """Запрещаем обновление поля задолженность"""
        if 'debt_to_supplier' in request.data:
            del request.data['debt_to_supplier']
        return super().update(request, *args, **kwargs)
