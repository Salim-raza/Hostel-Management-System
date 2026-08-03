from rest_framework import serializers
from .models import CustomUser, Profile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'role', 'password']
        read_only_fields = ['is_active', 'created_at', 'updated_at']
        
        def create(self, validated_data):
            user = CustomUser.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                role="student"
            
            )
            Profile.objects.create(
                user=user,
                phone_number=validated_data.get('phone_number'),
                date_of_birth=validated_data.get('date_of_birth'),
                address=validated_data.get('address')
            )
            return user
        
        # def validated_role(self, value):
        #     if value == 'admin' or value == 'controller' or value == 'assistant-controller' or value == 'manager':
        #         raise serializers.ValidationError("You cannot create a user with this role.")
            
            
    def validate_role(self, value):
                if value in ["admin", "controller", "assistant-controller", "manager"]:
                    raise serializers.ValidationError(
                        "You cannot create a user with this role."
                    )
                return value