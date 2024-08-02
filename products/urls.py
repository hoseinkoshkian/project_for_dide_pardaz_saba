
from django.urls import path
from django.views.generic import TemplateView
from .views import *
from .views import *
urlpatterns = [
    path('', TemplateView.as_view(template_name="Store.html") , name='store' ) ,
    #product
    path('newProduct', ProcutsView.as_view() , name='newProduct'),
    path('ProductFilter', Products_list_filter_View.as_view(), name='productFilter')
]
