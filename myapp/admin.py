from django.contrib import admin
from myapp.models import products,Order,Wishlist
# Register your models here.
admin.site.register(products)
admin.site.register(Order)
admin.site.register(Wishlist)