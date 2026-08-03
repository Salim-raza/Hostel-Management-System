from django.contrib.auth.models import AbstractUser
from .usermanage import CustomUserManager
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    role_choices = (
        ('admin', 'Admin'),
        ('controller', 'Controller'),
        ('assistant-controller', 'Assistant Controller'),
        ('manager', 'Manager'),
        ('student', 'Student'),
    )
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, choices=role_choices, default='student')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    room_number = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"