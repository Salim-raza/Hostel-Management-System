from rest_framework import serializers
from .models import Seat


class SeatCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"
        read_only_field = ["create_at", "update_at"]