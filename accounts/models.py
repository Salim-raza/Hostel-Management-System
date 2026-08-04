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
    