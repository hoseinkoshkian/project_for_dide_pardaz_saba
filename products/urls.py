
from django.urls import path
from django.views.generic import TemplateView
from .views import *
urlpatterns = [
    path('store', TemplateView.as_view(template_name="Store.html") , name='store' )
]
