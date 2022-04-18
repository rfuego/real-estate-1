from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from mainbase.models import MainBase

class MainBaseSerializer(ModelSerializer):
    class Meta:
        model = MainBase
        fields = ['type', 'numbers_flat', 'price', 'square_meters', 'address', 'metro', 'bath_room', 'balcon', 'holders']