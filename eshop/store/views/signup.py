from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.costumer import Costumer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        values = {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password}

        costumer = Costumer(firstname=first_name, lastname=last_name, email=email, password=password)

        # valideating user
        error = self.validate_user(costumer)
        if not error:
            if costumer.is_exits():
                error = "costumer exists for that email"
                return render(request, 'signup.html', {'error': error})
            else:
                costumer.password = make_password(costumer.password)
                messages.success(request, "signup successful")
                costumer.save()
                return HttpResponseRedirect("/")
        else:
            return render(request, 'signup.html', {'error': error, 'values': values})

    def validate_user(self, costumer):
        error = {}
        if not costumer.firstname:
            error = "first name required"
        elif len(costumer.firstname) < 4:
            error = "enter the name more then 4 words"

        if not costumer.lastname:
            error = "lastname required"
        elif len(costumer.lastname) < 4:
            error = "length of last name should be more then four"
        if len(costumer.password) < 5:
            error = "password is weak give more than 5 word"
        return error
