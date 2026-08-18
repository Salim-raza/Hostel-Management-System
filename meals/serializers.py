from rest_framework import serializers
from .models import Meal


class MealAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"
        read_only_fields = ["create_at"]
        