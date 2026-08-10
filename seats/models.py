from django.db import models
from django.conf import settings

# Create your models here.
class Seat(models.Model)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room_number = models.CharField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("available", "Available"),
            ("occupied", "Occupied"),
        ],
        default="available"
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)