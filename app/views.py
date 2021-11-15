from django.shortcuts import render
from django.views import View
from .models import *
from .forms import CustomerRegistrationForm
from django.contrib import messages

class ProductView(View):
    def get(self, request):
        mobiles = Product.objects.filter(category= 'M')
        laptops = Product.objects.filter(category= 'L')
        topwears = Product.objects.filter(category= 'TW')
        bottomwears = Product.objects.filter(category= 'BW')
        cameras = Product.objects.filter(category= 'CM')
        watches = Product.objects.filter(category= 'W')
        bags = Product.objects.filter(category= 'B')
        cosmetics = Product.objects.filter(category= 'C')
        return render(request, 'app/home.html', {'mobiles': mobiles, 'laptops': laptops, 
            'topwears': topwears, 'bottomwears': bottomwears, 'cameras': cameras, 'watches': watches, 'bags': bags, 'cosmetics': cosmetics})

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk = pk)
        return render(request, 'app/product_detail.html', {'product': product})
        

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def PasswordReset(request):
 return render(request, 'app/password_reset.html')

def mobile(request, data = None):
    if data == None:
        mobiles = Product.objects.filter(category= 'M')
    elif data =='Xiaomi' or data =='Samsung' or data =='Realme' or data =='Vivo' or data =='OnePlus':
        mobiles = Product.objects.filter(category= 'M').filter(brand = data)
    elif data == 'below':
        mobiles = Product.objects.filter(category= 'M').filter(discounted_price__lt=20000)
    elif data == 'above':
        mobiles = Product.objects.filter(category= 'M').filter(discounted_price__gt=20000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})

def laptop(request, data = None):
    if data == None:
        laptops = Product.objects.filter(category= 'L')
    elif data =='HP' or data =='Asus' or data =='Lenovo' or data =='Walton' or data =='Acer' or data == 'Avita':
        laptops = Product.objects.filter(category= 'L').filter(brand = data)
    elif data == 'below':
        laptops = Product.objects.filter(category= 'L').filter(discounted_price__lt=40000)
    elif data == 'above':
        laptops = Product.objects.filter(category= 'L').filter(discounted_price__gt=40000)
    return render(request, 'app/laptop.html', {'laptops': laptops})

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customer_registration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!!! Registered Successfully....')
            form.save()
        return render(request, 'app/customer_registration.html', {'form':form})
    
def checkout(request):
 return render(request, 'app/checkout.html')

def TopWear(request, data = None):
    if data == None:
        topwears = Product.objects.filter(category= 'TW')
    elif data =='MH_Fashion' or data =='ABC_Garments' or data =='XYZ_Shop' or data =='Freedom':
        topwears = Product.objects.filter(category= 'TW').filter(brand = data)
    return render(request, 'app/twear.html', {'topwears': topwears})

def BottomWear(request, data = None):
    if data == None:
        bottomwears = Product.objects.filter(category= 'BW')
    elif data =='MH_Fashion' or data =='ABC_Garments':
        bottomwears = Product.objects.filter(category= 'BW').filter(brand = data)
    return render(request, 'app/bwear.html', {'bottomwears': bottomwears})

def Camera(request):
 return render(request, 'app/camera.html')

def Watch(request):
 return render(request, 'app/watch.html')

def Cosmetics(request):
 return render(request, 'app/cosmetics.html')

def Bag(request):
 return render(request, 'app/bag.html')