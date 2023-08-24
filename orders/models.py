from django.db import models

# Create your models here.
class Order(models.Model):  # a single order includes multiple order items
    user = models.ForeignKey('myuser.CustomUser', on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product', through='OrderItem')  # Using the OrderItem model as an intermediary)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model): #a single item
    vendor = models.ForeignKey('myuser.Vendor', on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order {self.order.id}"
    