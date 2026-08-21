from rest_framework import serializers
from .models import Fine


class FineAddSerializer(serializers.ModelSerializer):
    class Meta:
         model = Fine
         fields = ['student', 'amount', 'reason', 'dou_date', 'is_paid', 'paid_at']
         read_only_fields = ['create_at']