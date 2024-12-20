from django.contrib import admin

from .models import Product, SalesItem, SalesRecord


# Register your models here.
@admin.register(SalesRecord)
class SalesRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(SalesItem)
class SalesItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
