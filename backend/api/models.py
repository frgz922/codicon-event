
from django.db import models

#models

class Contact(models.Model):
    name= models.CharField(max_length=50)
    email = models.EmailField()
    message=models.TextField()
    
    def __str__(self) -> str:
        return self.number_phone

class Packages(models.Model):
    name = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=250, null=True)
    icon = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name
    
    
class Destinations(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class BoxData(models.Model):

    class packageTypes(models.TextChoices):
        ATAUD = 'ataud'
        REGALO = 'regalo'
        CAJA =  'caja'
        CAJA_FUERTE = 'caja fuerte'
    
    class finalDestinations(models.TextChoices):
        ENTERRAR = 'enterrar'
        QUEMAR = 'quemar'
        GUARDAR = 'guardar'
        REGALAR = 'regalar'

    class paymentMethods(models.TextChoices):
        TRANSFERENCIA = 'transferencia'
        PAYPAL = 'zelle'
        PAGO_MOVIL = 'pagomovil'


    letterContent = models.TextField()
    packageType = models.CharField(choices=packageTypes.choices, default=packageTypes.CAJA, max_length=50)
    finalDestination = models.CharField(choices=finalDestinations.choices, default=finalDestinations.ENTERRAR, max_length=50)
    recipientName = models.CharField(max_length=250, null=True)
    recipientAddress = models.CharField(max_length=250, null=True)
    recipientPhone = models.CharField(max_length=250, null=True)
    clientName = models.CharField(max_length=250)
    clientPhone = models.CharField(max_length=250)
    clientEmail = models.CharField(max_length=250)
    paymentMethod = models.CharField(choices=paymentMethods.choices, default=paymentMethods.TRANSFERENCIA, max_length=50)
    confirmationNumber = models.CharField(max_length=250, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.clientName
    

class BoxDataImage(models.Model):
    boxData = models.ForeignKey(BoxData, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.boxData.clientName