from rest_framework import serializers

from .models import BoxData,Packages,Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields= '__all__'
        
    def to_representation(self, instance):
        return{
            'name': instance.name,
            'number_phone': instance.number_phone,
        }

class BoxDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxData
        fields = ('id', 'letterContent', 'image', 'packageType', 'finalDestination', 'recipientName', 'recipientAddress', 'recipientPhone', 'clientName', 'clientAddress', 'clientPhone', 'clientEmail', 'paymentMethod')
 
    def to_representation(self, instance):
        return {
            'clientName': instance.clientName,
            'clientAddress': instance.clientAddress,
        }
    
    def create(self, validated_data):
        return BoxData.objects.create(**validated_data)
    
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ('id','name','dimensions','price','description')
 
    def to_representation(self, instance):
        return {
            'name': instance.name,
            'price': instance.price,
        }