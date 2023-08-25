from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    PRODUCT_CATEGORIES = (
    ('skincare', 'Skin Care'),
    ('clothing', 'Clothing'),
    ('fashion', 'Fashion'),
    # Add more categories as needed
)
    name = models.CharField(max_length=50, choices=PRODUCT_CATEGORIES)

    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    name = models.CharField( max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self) -> str:
        return f"{self.name} is {self.price} GHS"
class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField( max_length=50)
    phone = models.CharField(max_length=50, default="", blank=True)
    quantity = models.SmallIntegerField(default=1)
    date = models.DateTimeField(default=datetime.datetime.today)
    shipped = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.customer.username} shipped {self.product.name}"
