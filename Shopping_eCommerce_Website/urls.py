from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('product1-detail/', views.product_1_detail, name='product-detail'),
    path('product2-detail/', views.product_2_detail, name='product-detail'),
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
]