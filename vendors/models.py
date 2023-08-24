from django.db import models
from myuser.models import Vendor


from django.db import models

class VendorProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0) 

    vendor = models.ForeignKey('myuser.Vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
