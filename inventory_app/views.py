from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    
    context = {
        'products': products
        }
    return render(request, 'inventory/product_list.html', context)