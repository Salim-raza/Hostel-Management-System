from rest_framework import serializers
from .models import *

class ProfileUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'division', 'district', 'upazila', 'room_number', 'date_of_birth', 'address', 'image', 'created_at', 'updated_at']
        read_only_fields = ["created_at", "updated_at"]
        
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.delete_image = validated_data.get('delete_image', False)
        return super().update(instance, validated_data)