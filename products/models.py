from django.db import models
from myuser.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey('myuser.Vendor', on_delete=models.CASCADE)  # Add this line
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    quantity = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        product_names = ", ".join([product.name for product in self.products.all()])
        return f"User: {self.user.username}, Products: {product_names}, Quantity: {self.quantity}"