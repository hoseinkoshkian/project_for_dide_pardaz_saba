from django.shortcuts import render
from rest_framework.views import APIView
from products.models import *
from rest_framework.response import Response
from .serializers import mobielSerializer

class ProductView(APIView):
    def get(self, request):
        brand_query = request.GET.get('brand') # بر اساس نام
        if brand_query != None:
            find_brand = brand.objects.filter(name=brand_query).count()
            if find_brand == 0 :
                res = {
                    'msg' : 'هیج محصولی با این برند یافت نشد'
                }
                return Response(res , 404)
            products_data = mobile.objects.filter( brand=find_brand )
        data = mobielSerializer(products_data, many=True)
        return Response(data.data , 200)
