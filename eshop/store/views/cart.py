from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.costumer import Costumer
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self, request):
        cart_ids=list(request.session.get('cart').keys())
        product=Product.get_product_by_session_id(cart_ids)
        print(product)
        return render(request, 'orders/cart.html',{'products':product})