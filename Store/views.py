from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def homepage(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'store/index.html', context)
    # return render(request, response)

def detailpage(request, input_id):
    current_product = Product.objects.get(id=input_id)
    context = {'current_product': current_product}
    return render(request, 'store/detail.html', context)
