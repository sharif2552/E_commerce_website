from django.db import models

# Create your models here.
from django.db import models
from myuser.models import CustomUser  # Import the CustomUser model
from products.models import Product  # Import the Product model
from products.models import Address

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE , null = True, blank = True)
    Total = models.IntegerField(null=True, blank = True)
    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order {self.order.id}"
