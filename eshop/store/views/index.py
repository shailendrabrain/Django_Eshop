from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.costumer import Costumer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.views import View


class Index(View):
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None
        categoryId = request.GET.get('category')

        if categoryId:
            products = Product.get_all_products_by(categoryId)
        else:
            products = Product.get_all_objects()
        categories = Category.get_all_categories()
        

        return render(request, 'index.html', {'products': products, 'categories': categories})
            
    def post(self,request):
        product=request.POST.get('product_id')
        remove=request.POST.get('removetocart')
        
        #product=Product.get_product_by_id(product_id)
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:    
                        cart[product]=quantity-1
                else:
                    cart[product]=1+quantity    
            else:
                cart[product]=1    
        else:
            cart={}
            cart[product]=1  
        request.session['cart']=cart  
        print(request.session['cart'])    
        return HttpResponseRedirect("/")

