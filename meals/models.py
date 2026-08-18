from django.db import models
from django.conf import settings

# Create your models here.
class Meal(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    is_taken = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.email} - {self.data} - {self.meal_type}"