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
    country = models.ForeignKey(country , on_delete=models.CASCADE)
    addBy = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    addOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class mobile(models.Model):
    modelName = models.CharField(max_length=100 , unique=True)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE , related_name='brand')
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    screenSize = models.PositiveIntegerField(max_length=10)
    inventoryStatus =models.BooleanField(default=True)
    addOn = models.DateTimeField(auto_now_add=True)
    addBy = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    manufacturingCountry = models.ForeignKey(country, on_delete=models.CASCADE)
    def __str__(self):
        return self.modelName