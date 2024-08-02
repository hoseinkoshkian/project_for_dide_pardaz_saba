from rest_framework import serializers
from products.models import mobile


class mobielSerializer(serializers.ModelSerializer):
  class Meta():
      model = mobile
      fields = ('modelName' , 'brand' , 'color' , 'price' , 'manufacturingCountry' , 'inventoryStatus')