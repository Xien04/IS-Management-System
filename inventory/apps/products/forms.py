from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "supplier",
            "name",
            "sku",
            "category",
            "unit_price",
            "cost_price",
            "description",
            "is_active"
        ]