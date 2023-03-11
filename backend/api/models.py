
from django.db import models

#models

class Contact(models.Model):
    name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    number_phone=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.number_phone

class Packages(models.Model):
    name = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name
    
class Destinations(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class BoxData(models.Model):

    class packageTypes(models.TextChoices):
        URNA = 'urna'
        REGALO = 'regalo'
        CAJA =  'caja'
        CAJA_FUERTE = 'caja fuerte'
    
    class finalDestinations(models.TextChoices):
        ENTERRAR = 'enterrar'
        QUEMAR = 'quemar'
        GUARDAR = 'guardar'
        REGALAR = 'regalar'

    class paymentMethods(models.TextChoices):
        EFECTIVO = 'efectivo'
        TARJETA = 'tarjeta'
        TRANSFERENCIA = 'transferencia'
        PAYPAL = 'paypal'
        PAGO_MOVIL = 'pagomovil'


    letterContent = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    packageType = models.CharField(choices=packageTypes.choices, default=packageTypes.CAJA, max_length=50)
    finalDestination = models.CharField(choices=finalDestinations.choices, default=finalDestinations.ENTERRAR, max_length=50)
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
    