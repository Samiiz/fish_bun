from django.contrib import admin

from .models import OrderRecord, RawMaterial, Stock, Supplier


# Register your models here.
@admin.register(OrderRecord)
class OrderRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass
