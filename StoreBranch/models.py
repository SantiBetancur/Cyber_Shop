from django.db import models

# Create your models here.

class Branch(models.Model):
    branchId = models.IntegerField(null=False,primary_key=True)
    address = models.CharField(max_length=45,null=False)

    def __str__(self):
        return str(self.branchId)
    
class Product(models.Model):
    productId = models.IntegerField(null=False,primary_key=True)
    price = models.FloatField(null=False)
    category = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    productBranchId = models.ForeignKey(Branch,null=False,on_delete=models.CASCADE)