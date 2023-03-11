from rest_framework import viewsets
from .serializers import BoxDataSerializer, PackageSerializer, ServiceSerializer
from .models import BoxData, Packages, Destinations

class BoxDataViewSet(viewsets.ModelViewSet):
    queryset = BoxData.objects.all().order_by('clientName') #querying database for all records
    serializer_class = BoxDataSerializer

class PackagesViewSet(viewsets.ModelViewSet):
    queryset = Packages.objects.all().order_by() #querying database for all records
    serializer_class = PackageSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Destinations.objects.all().order_by() #querying database for all records
    serializer_class = ServiceSerializer