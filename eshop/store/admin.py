from django.contrib import admin
from . models.product import Product
from. models.category import Category
from.models.costumer import Costumer
# Register your models here.
#@admin.register(Product)

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category','image']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']
    
admin.site.register(Product,AdminProduct)
admin.site.register(Category,CategoryAdmin)

@admin.register(Costumer)
class costumerAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email']
    
