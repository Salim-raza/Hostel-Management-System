from rest_framework import serializers
from .models import CustomUser

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'role', 'password', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['is_active', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role="student"
        )
        return user
        
    def validated_role(self, value):
        if value == 'admin' or value == 'controller' or value == 'assistant-controller' or value == 'manager':
            raise serializers.ValidationError("You cannot create a user with this role.")
            
class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()