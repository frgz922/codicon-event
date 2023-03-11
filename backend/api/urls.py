from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'box',views.BoxDataViewSet)
router.register(r'packages',views.PackagesViewSet)
router.register(r'services',views.ServicesViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', 
         include('rest_framework.urls',namespace='rest_framework'))
]