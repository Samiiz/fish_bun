from django.urls import path
from .views import OrderRecordView, SupplierView, RawMaterialView, StockView


urlpatterns = [
    path("suppliers/", SupplierView.as_view(), name="serppiers"),
    path("oerders/records/", OrderRecordView.as_view(), name="order-records"),
    path("raw_materials/", RawMaterialView.as_view(), name="raw-materials"),
    path("stocks/", StockView.as_view(), name="stocks"),
]