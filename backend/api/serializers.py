from rest_framework import serializers

from .models import BoxData,Packages,Destinations,Contact, BoxDataImage


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields= '__all__'
        
    def to_representation(self, instance):
        return{
            'name': instance.name,
            'message': instance.message,
        }
class BoxDataImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxDataImage
        fields = ('image',)

class BoxDataSerializer(serializers.ModelSerializer):

    images = BoxDataImageSerializer(source='boximage_set', many=True, read_only=True)
    recipientName = serializers.CharField(max_length=250, allow_blank=True)
    recipientPhone = serializers.CharField(max_length=250, allow_blank=True)
    recipientAddress = serializers.CharField(max_length=250, allow_blank=True)

    class Meta:
        model = BoxData
        fields = ('id', 'letterContent', 'images', 'packageType', 'finalDestination', 'recipientName', 'recipientAddress', 'recipientPhone', 'clientName', 'clientPhone', 'clientEmail', 'paymentMethod', 'confirmationNumber', 'total')
 
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'clientName': instance.clientName,
        }
    
    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        box = BoxData.objects.create(**validated_data)
        for image_data in images_data.values():
            BoxDataImage.objects.create(image=image_data, boxData=box)
        return box
    
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ('id','name','dimensions','price','description', 'icon')
 
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'price': instance.price,
            'description': instance.description,
            'icon': instance.icon,
            'dimensions': instance.dimensions,
        }
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = ('id','name','price','description')
 
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'price': instance.price,
            'description': instance.description,
        }
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)