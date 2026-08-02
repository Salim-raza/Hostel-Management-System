from rest_framework import serializers
from .models import CustomUser, Profile



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'role', 'password', 'phone_number', 'date_of_birth', 'address']
        read_only_fields = ['is_active', 'is_staff']
        
        def create(self, validated_data):
            user = CustomUser.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                role=validated_data['role'],
                phone_number=validated_data['phone_number'],
                date_of_birth=validated_data['date_of_birth'],
                address=validated_data['address']
            )
        
        def validated_role(self, value):
            if value == 'admin' or value == 'controller' or value == 'assistant-controller':
                raise serializers.ValidationError("You cannot create a user with this role.")