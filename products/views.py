from django.shortcuts import render

# Create your views here.
from .models import products

def product_list(request):
    my_product = products.objects.all()
    return render(request, 'products/product_list.html', {'products': my_product})
