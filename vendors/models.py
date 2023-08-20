from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):  # a single order includes multiple order items
    
    products = models.ManyToManyField('products.Product', through='OrderItem')  # Using the OrderItem model as an intermediary)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model): #a single item
    vendor = models.ForeignKey('vendors.Vendor', on_delete=models.CASCADE)
    order = models.ForeignKey('vendors.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order {self.order.id}"
    
    from django.db import models

class VendorProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0) 

    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
