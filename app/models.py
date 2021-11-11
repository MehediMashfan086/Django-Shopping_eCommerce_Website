from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
    ('Barisal','Barisal'),
    ('Chittagong','Chittagong'),
    ('Comilla','Comilla'),
    ('Dhaka North','Dhaka North'),
    ('Dhaka South','Dhaka South'),
    ('Gazipur','Gazipur'),
    ('Khulna','Khulna'),
    ('Mymensingh','Mymensingh'),
    ('Narayanganj','Narayanganj'),
    ('Rajshahi','Rajshahi'),
    ('Rangpur','Rangpur'),
    ('Sylhet','Sylhet'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

def __str__(self):
    return str(self.id)

CATAGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
    ('CM','Camera'),
    ('W','Watch'),
    ('B','Bag'),
    ('C','Cosmetics'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    catagory = models.CharField(choices=CATAGORY_CHOICES, max_length=10)
    product_image = models.ImageField(upload_to = 'productimg')

def __str__(self):
    return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

def __str__(self):
    return str(self.id)

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The way','On The way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Pending')
