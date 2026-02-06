from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length = 200)
    contact_name = models.CharField(max_length = 200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
