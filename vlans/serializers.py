from rest_framework import serializers
from .models import Vlans, CoreSubnets

class VlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vlans
        fields = '__all__'

class CoreSubnetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreSubnets
        fields = '__all__'
