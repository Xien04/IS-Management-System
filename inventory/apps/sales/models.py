from decimal import Decimal

from django.db import models

class Sale(models.model):
    customer_name = models.charField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    sales_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-sale_date"]

    def __str__(self) -> str:
        return f"Sale #{self.pk}"
    
    @property
    def total(self) -> Decimal:
        return sum((item.line_total for item in self.items.all()), Decimal("0.00"))
    

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_date=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.product.name} x {self.quantity}"
    
    @property
    def line_total(self) -> Decimal:
        return self.unit_price * self.quantity
