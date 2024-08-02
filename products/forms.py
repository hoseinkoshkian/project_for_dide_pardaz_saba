from django import forms

from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = mobile
        fields = ('modelName' ,'brand' , 'price' , 'color' , 'screenSize' , 'manufacturingCountry' , 'inventoryStatus' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelName'].widget.attrs['class'] = 'form-control'

        self.fields['brand'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['color'].widget.attrs['class'] = 'form-control'
        self.fields['screenSize'].widget.attrs['class'] = 'form-control'
        self.fields['inventoryStatus'].widget.attrs['class'] = 'mt-5'
        self.fields['manufacturingCountry'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['placeholder'] = 'product price'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
    #         visible.field.widget.attrs['placeholder'] = visible.field.label