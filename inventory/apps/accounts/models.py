from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=32, blank=True)
    role = models.CharField(max_length=64, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} Profile"
