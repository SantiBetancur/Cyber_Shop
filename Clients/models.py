from django.db import models

# Create your models here.

class ClientInfo(models.Model):
    clientName = models.CharField(max_length=50)
    clientAddress = models.CharField(max_length=75)

class clientPhones(models.Model):
    idClient = models.ForeignKey(ClientInfo,null=False,on_delete=models.CASCADE)
    phoneNumber = models.IntegerField(null=False)

class Corporation(ClientInfo):
    RUT = models.IntegerField(null=False,primary_key=True)
    discount = models.FloatField()

class Person(ClientInfo):
    DNI = models.IntegerField(null=False,primary_key=True)


class historyPerson(ClientInfo):
    DNI = models.IntegerField(null=False)

class historyCorp(ClientInfo):
    RUT = models.IntegerField(null=False)
    discount = models.FloatField()