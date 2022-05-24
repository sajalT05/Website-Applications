from rest_framework import serializers

# import class from models
from .models import DRFapi

class APIserializer(serializers.ModelSerializer):
    class Meta:
        model=DRFapi
        fields='__all__'