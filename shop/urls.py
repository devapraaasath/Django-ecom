from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('logout',views.logout_page,name='logout'),
    path('login',views.login_page,name='login'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('cart_page',views.cart_page,name='cart_page'),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('fav',views.fav_cart,name="fav"),
    path('fav_page',views.fav_page,name="fav_page"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('contact',views.contact_us,name="contact"),

] 