
from django.db import models
#models
class BoxData(models.Model):

    class paymentMethods(models.TextChoices):
        EFECTIVO = 'efectivo'
        TARJETA = 'tarjeta'
        TRANSFERENCIA = 'transferencia'
        PAYPAL = 'paypal'
        PAGO_MOVIL = 'pagomovil'


    letterContent = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    packageType = models.ForeignKey('packages', on_delete=models.CASCADE)
    finalDestination = models.ForeignKey('destinations', on_delete=models.CASCADE)
    recipientName = models.CharField(max_length=250)
    recipientAddress = models.CharField(max_length=250)
    recipientPhone = models.CharField(max_length=250)
    clientName = models.CharField(max_length=250)
    clientAddress = models.CharField(max_length=250)
    clientPhone = models.CharField(max_length=250)
    clientEmail = models.CharField(max_length=250)
    paymentMethod = models.CharField(choices=paymentMethods.choices, default=paymentMethods.TRANSFERENCIA, max_length=50)

    def __str__(self):
        return self.clientName
    
    

class Packages(models.Model):
    name: models.CharField(max_length=50)
    dimensions: models.CharField(max_length=50)
    price: models.CharField(max_length=50)
    description: models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Destinations(models.Model):
    name: models.CharField(max_length=50)
    price: models.CharField(max_length=50)
    description: models.CharField(max_length=250)

    def __str__(self):
        return self.name