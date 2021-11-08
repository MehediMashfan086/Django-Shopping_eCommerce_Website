from django.urls import path
from app import views
from app.views import *
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('laptop/', views.laptop, name='laptop'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('twear/', views.TopWear, name='twear'),
    path('bwear/', views.BottomWear, name='bwear'),
    path('camera/', views.Camera, name='camera'),
    path('watch/', views.Watch, name='watch'),
    path('cosmetics/', views.Cosmetics, name='cosmetics'),
    path('bag/', views.Bag, name='bag'),
]