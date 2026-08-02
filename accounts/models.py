from django.db import models

# Create your models here.
class CustomUser(models.Model):
    role_choices = (
        ('admin', 'Admin'),
        ('controller', 'Controller'),
        ('assistant-controller', 'Assistant Controller'),
        ('student', 'Student'),
    )
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=role_choices, default='student')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    room_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"