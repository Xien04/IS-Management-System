from django import forms

from apps.products.models import Product

from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = [
            "product",
            "quantity_on_hand",
            "reorder_level",
            "location",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        existing = InventoryItem.objects.values_list("product_id", flat=True)
        if self.instance and self.instance.pk:
            self.fields["product"].queryset = Product.objects.filter(
                id=self.instance.product_id
            ) | Product.objects.exclude(id_in = existing)
        else:
            self.fields["product"].queryset = Product.objects.exclude(id_in=existing)