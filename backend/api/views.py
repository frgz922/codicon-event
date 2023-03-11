from rest_framework import viewsets
from .serializers import BoxDataSerializer, PackageSerializer
from .models import BoxData, Packages

class BoxDataViewSet(viewsets.ModelViewSet):
    queryset = BoxData.objects.all().order_by('clientName') #querying database for all records
    serializer_class = BoxDataSerializer

class PackagesViewSet(viewsets.ModelViewSet):
    queryset = Packages.objects.all().order_by() #querying database for all records
    serializer_class = PackageSerializer