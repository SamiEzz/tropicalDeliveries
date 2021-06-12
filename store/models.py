from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class globalConfig(models.Model):
    name = models.CharField(max_length=200,default="Tropical Deliveries")
    year = models.CharField(max_length=200,default="2021")
    title = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Provider(models.Model):
    name = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    openinghours = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    price = models.FloatField()
    providerId = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200)
    avatar = models.CharField(max_length=200, default="")
    nborders = models.IntegerField(default="0")

    def __str__(self):
        return self.username


class Cart(models.Model):
    CostumerID = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    NumberOfProducts = models.CharField(max_length=200)
    ProductIDs = models.CharField(max_length=200, default="")
    TotalPrice = models.FloatField()

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    CostumerID = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    CartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    isOngoing = models.CharField(max_length=200, default="")
    DeliveryArea = models.CharField(max_length=200, default="")
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True, default="")

    def __str__(self):
        return str(self.id)


class Incident(models.Model):
    CostumerID = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    CartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True, default="")
    issue = models.TextField(max_length=500, default="")

    def __str__(self):
        return str(self.id)