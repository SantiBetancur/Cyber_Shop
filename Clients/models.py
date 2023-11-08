from django.db import models

# Create your models here.

class ClientInfo(models.Model):
    idClient = models.IntegerField(null=False)
    clientName = models.CharField(max_length=50)
    clientAddress = models.CharField(max_length=75)

class clientPhones(models.Model):
    idClient = models.ForeignKey(ClientInfo,null=False,on_delete=models.CASCADE)
    phoneNumber = models.IntegerField(null=False)

class Corporation(models.Model):
    RUT = models.IntegerField(null=False,primary_key=True)
    idClient = models.ForeignKey(ClientInfo,null=False,on_delete=models.CASCADE)
    discount = models.FloatField()

class Person(models.Model):
    DNI = models.IntegerField(null=False,primary_key=True)
    idClient = models.ForeignKey(ClientInfo,null=False,on_delete=models.CASCADE)