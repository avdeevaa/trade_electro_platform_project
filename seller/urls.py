from django.urls import path

from seller.apps import SellerConfig
from seller.views import NetworkNodeListAPIView, SupplierDestroyAPIView, SupplierRetrieveAPIView, SupplierCreateAPIView, \
    SupplierListAPIView, NetworkNodeUpdateAPIView, SupplierUpdateAPIView

app_name = SellerConfig.name

urlpatterns = [
    path("suppliers/", SupplierListAPIView.as_view(), name="suppliers-all"),
    path("suppliers/create/", SupplierCreateAPIView.as_view(), name="suppliers-create"),
    path("suppliers/<int:pk>/", SupplierRetrieveAPIView.as_view(), name="suppliers-retrieve"),
    path("suppliers/update/<int:pk>/", SupplierUpdateAPIView.as_view(), name="suppliers-update"),
    path("suppliers/delete/<int:pk>/", SupplierDestroyAPIView.as_view(), name="suppliers-delete"),

    path("networknode/", NetworkNodeListAPIView.as_view(), name='all-networknode'),
    path("networknode/update/", NetworkNodeUpdateAPIView.as_view(), name="networknode-update"),
]