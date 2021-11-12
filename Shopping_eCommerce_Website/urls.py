from django.urls import path
from app import views
from app.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ProductView.as_view(), name = 'home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
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
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)