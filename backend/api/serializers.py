from rest_framework import serializers

from .models import BoxData

class BoxDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxData
        fields = ('id', 'letterContent', 'images', 'packageType', 'finalDestination', 'recipientName', 'recipientAddress', 'recipientPhone', 'clientName', 'clientAddress', 'clientPhone', 'clientEmail', 'paymentMethod')
 
    def to_representation(self, instance):
        return {
            'clientName': instance.clientName,
            'clientAddress': instance.clientAddress,
        }
    
    def create(self, validated_data):
        return BoxData.objects.create(**validated_data)