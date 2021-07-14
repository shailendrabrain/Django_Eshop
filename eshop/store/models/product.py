from django.db import models
from store.models.category import Category



class Product(models.Model):
    name=models.CharField( max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1, null=True)
    description=models.CharField( max_length=230)
    image=models.ImageField( upload_to='upload/product/')
    
    
    @staticmethod
    def get_all_objects():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by(categories_id):
        if categories_id:
            return Product.objects.filter(category=categories_id)
        else:
            return Product.get_all_objects()
    
    @staticmethod
    def get_product_by_id(product_id):
        return Product.objects.get(id=product_id)
        
    @staticmethod
    def get_product_by_session_id(ids):
        return Product.objects.filter(id__in=ids)    