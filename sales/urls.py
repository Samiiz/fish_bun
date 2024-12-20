from django.urls import path

from .views import ProductView, SaleRecordView, SalesItemView

urlpatterns = [
    path("products/", ProductView.as_view(), name="products"),
    path("sales/records/", SaleRecordView.as_view(), name="sales-records"),
    path("sales/record/items/", SalesItemView.as_view(), name="sales-items"),
]
