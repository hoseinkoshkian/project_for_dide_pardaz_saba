from django.shortcuts import render
from django.views import View
from products.forms import ProductForm
from .models import mobile
from django.db.models import F
class ProcutsView(View):
    form = ProductForm()
    def get(self, request, *args, **kwargs):
        productlist = mobile.objects.all()
        context = {'newProductForm': self.form ,
                   'productlist': productlist}
        return  render(request , 'Store.html' , context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.addBy = request.user
            form.save()

        context = {'newProductForm': self.form}
        return  render(request , 'Store.html' , context)

class Products_list_filter_View(View):
    def post(self, request, *args, **kwargs):
        filter_data = request.POST['searchByName']
        if (request.POST.get('id_checkbox') == "on"):
            matching_mobiles = mobile.objects.filter(manufacturingCountry=F('brand__country'))
            return render(request, 'search.html', {'productlist': matching_mobiles })

        productlist = mobile.objects.filter(modelName__contains=filter_data)
        return render(request , 'search.html' , {'productlist': productlist})