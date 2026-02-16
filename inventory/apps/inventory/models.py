from django.db import models

class InventoryItem(models.Model):
    product = models.OneToOneField(
        "products.Product",
        on_delete = models.CASCADE,
        related_name = "inventory",
    )
    quantity_on_hand = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)
    location = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_no=True)

    class Meta:
        ordering = ["product_name"]


    @property
    def low_stock(self) -> bool:
        return self.quantity_on_hand <= self.reorder_level
