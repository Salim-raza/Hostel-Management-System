from django.db import models
from django.conf import settings

# Create your models here.
class Fine(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    reason = models.CharField(max_length=250, blank=True)
    dou_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.email} - {self.amount}"