from rest_framework import viewsets
from .serializers import BoxDataSerializer
from .models import BoxData

class BoxDataViewSet(viewsets.ModelViewSet):
    queryset = BoxData.objects.all().order_by('clientName') #querying database for all records
    serializer_class = BoxDataSerializer