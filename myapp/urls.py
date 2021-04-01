from django.contrib import admin
from django.urls import path,include
from . import views
<<<<<<< HEAD
urlpatterns = [
    path('',views.index,name='index'),
    path('cart.html',views.cart,name='cart'),
    path('checkout.html',views.checkout,name='checkout'),
    path('shop.html',views.shop,name='shop'),
    path('single-product.html',views.single,name='single-product'),
    ]
=======

app_name = "myapp"

urlpatterns = [
     
     path('index/',views.index,name='index'),
     path('cart/',views.cart,name='cart'),
     path('checkout/',views.checkout,name='checkout'),
     path('shop/<field>/<value>/',views.shop,name='shop'),
     path('single-product/<id>/<catageory>/',views.singleproduct,name='single-product'),
     path('signup/',views.signup,name='signup'),
     path('signin/',views.signin,name='signin'),
     path('signout/',views.signout,name='signout'),
     path('add_to_cart/<int:id>/',views.add_to_card,name='add_to_card'),
     path('item_clear/<int:id>/',views.item_clear,name='item_clear'),
     path('cart_clear/',views.cart_clear,name='cart_clear'),
     path('addProduct/',views.addProduct,name='addProduct'),
     path('search/',views.search,name='foo-search'),
     path('wishlist/<id>/',views.wishlist,name='wishlist'),
     path('showWishlist/',views.show_wishlist,name='showWishlist'),
     path('place_order/',views.place_order,name='place_order'),
     path('',views.index,name='index'),   
    ]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()    
>>>>>>> 6398115 (yes)
