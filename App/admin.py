from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')

class ProductAdmin(admin.ModelAdmin):
    prodeuct_display=('name','product_mage','selling_price')

admin.site.register(Catagory,CategoryAdmin)
# admin.site.register(Catagory)
admin.site.register(Product,ProductAdmin)