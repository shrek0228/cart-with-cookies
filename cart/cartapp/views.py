from django.shortcuts import render
from django.http import JsonResponse
from cartapp.models import *
# Create your views here.
def show_products(request):
    response = render(request,"products.html",context={"products": Product.objects.all()})
    if request.method == "POST":
        if "product_pk" not in request.COOKIES: #
            new_product = request.POST.get('product_pk') #
            response.set_cookie('product_pk',new_product) #
            return response #
        else: #
            new_product = request.COOKIES['product_pk'] + " " + request.POST.get('product_pk') # "1" + " " + "2"  = "1 2"
            response.set_cookie('product_pk',new_product) #
            return response #

    return response

def show_cart(request):
    products_pk = request.COOKIES.get('product_pk', '').split(' ')
    if request.method == 'POST':
        index = int(request.POST.get('index'))
        products_pk.pop(index)

    list_products = []
    for product_pk in products_pk:
        list_products.append(Product.objects.get(pk=product_pk))
    response = render(request,"cart.html",context={"products": list_products})
    
    if request.method == 'POST':
        response.set_cookie('product_pk', ' '.join(products_pk))
    
    return response
