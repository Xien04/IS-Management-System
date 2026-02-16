from django.contrib import admin

from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity_on_hand", "reorder_level", "location", "updated_at")
    list_filter = ("location")
    search_field = ("product_name", "product_sku")