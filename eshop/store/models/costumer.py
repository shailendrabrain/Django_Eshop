from django.db import models

class Costumer(models.Model):
    firstname=models.CharField( max_length=50)
    lastname=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
    
    
    def is_exits(self):
        if Costumer.objects.filter(email=self.email):
            return True
        
        return False
    
    @staticmethod
    def get_costumer_by_email(email):
        try:
            return Costumer.objects.get(email=email)
        except:
            return False