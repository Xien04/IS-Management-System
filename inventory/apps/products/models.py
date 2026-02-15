from django.db import models

# Create your models here.
class Product(models.Model):
    supplier = models.ForeignKey(
        "suppliers.Supplier",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name = "products",
    )
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.sku})"