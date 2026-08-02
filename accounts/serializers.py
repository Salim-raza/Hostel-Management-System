from rest_framework import serializers
from .models import CustomUser, Profile



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'role', 'password', 'phone_number', 'date_of_birth', 'address']
        read_only_fields = ['is_active', 'is_staff']