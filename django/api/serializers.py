from rest_framework import serializers
from mainApp.models import apiItems

class apiItemserializers(serializers.ModelSerializer):
    class Meta:
        model=apiItems
        fields='__all__'