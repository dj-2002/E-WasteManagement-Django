from django.contrib import admin
<<<<<<< HEAD
from myapp.models import products
# Register your models here.
admin.site.register(products)
 
=======
from myapp.models import products,Order,Wishlist
# Register your models here.
admin.site.register(products)
admin.site.register(Order)
admin.site.register(Wishlist)
>>>>>>> 6398115 (yes)
