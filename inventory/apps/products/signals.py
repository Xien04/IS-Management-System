from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.inventory.models import InventoryItem

from .models import Product

@receiver(post_save, sender=Product)
def create_inventory_item(sender, instance, created, **kwargs):
    if created:
        InventoryItem.objects.get_or_create(product=instance)