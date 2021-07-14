from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.costumer import Costumer
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.views import View

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        costumer = Costumer.get_costumer_by_email(email)
        print()
        error = None
        if costumer:
            if check_password(password, costumer.password):
                messages.success(request, "login successful")
                request.session['costumer']=costumer.id 
                request.session['email']=costumer.email
                return HttpResponseRedirect("/")
            else:
                error = "password does not match"
                return render(request, 'login.html', {'error': error})
        else:
            error = 'costumer does not exits '
            return render(request, 'login.html', {'error': error})

def Logout(request):
    request.session.clear()
    return HttpResponseRedirect("/")
    
