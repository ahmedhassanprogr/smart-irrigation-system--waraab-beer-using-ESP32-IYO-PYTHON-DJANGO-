from rest_framework import serializers
from .models import PumbStatus

class PumbStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumbStatus
        fields = "__all__"