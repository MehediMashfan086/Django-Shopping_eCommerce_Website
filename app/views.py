from django.shortcuts import render

def home(request):
 return render(request, 'app/home.html')

def product_1_detail(request):
 return render(request, 'app/product_1_detail.html')

def product_2_detail(request):
 return render(request, 'app/product_2_detail.html')

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

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def laptop(request):
 return render(request, 'app/laptop.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

def TopWear(request):
 return render(request, 'app/laptop.html')

def BottomWear(request):
 return render(request, 'app/laptop.html')