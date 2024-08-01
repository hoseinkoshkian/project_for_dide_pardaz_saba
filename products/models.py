from django.db import models
from django.contrib.auth import get_user_model

class country(models.Model):
    name = models.CharField(max_length=100)
    addBy = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    addOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    addBy = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    addOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class mobile(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE , related_name='brand')
    price = models.IntegerField()
    color = models.CharField(max_length=100)
    screenSize = models.IntegerField(max_length=10)
    inventoryStatus =models.BooleanField(default=True)
    addOn = models.DateTimeField(auto_now_add=True)
    manufacturingCountry = models.ForeignKey(country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name