from django.contrib import admin

from .models import Sale, SaleItem

class SaleItemInLine(admin.TabularInline):
    model = SaleItem
    extra = 0

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "customeer_name", "sale_date")
    search_fields = ("customer_name")
    inlines = [SaleItemInLine]

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ("sale", "product", "quantity", "unit_price")
    search_fields = ("sale__id", "product__name", "product__sku")