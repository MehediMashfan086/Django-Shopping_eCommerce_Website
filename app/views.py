from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductView(View):
    def get(self, request):
        totalitem = 0
        mobiles = Product.objects.filter(category= 'M')
        laptops = Product.objects.filter(category= 'L')
        topwears = Product.objects.filter(category= 'TW')
        bottomwears = Product.objects.filter(category= 'BW')
        cameras = Product.objects.filter(category= 'CM')
        watches = Product.objects.filter(category= 'W')
        bags = Product.objects.filter(category= 'B')
        cosmetics = Product.objects.filter(category= 'C')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/home.html', {'mobiles': mobiles, 'laptops': laptops, 
            'topwears': topwears, 'bottomwears': bottomwears, 'cameras': cameras, 'watches': watches, 
            'bags': bags, 'cosmetics': cosmetics, 'totalitem': totalitem})

class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk = pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(Q(product = product.id)
                                & Q(user=request.user)).exists()
        return render(request, 'app/product_detail.html', {'product': product,
            'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})
        

@login_required
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prodt_id')
 product=Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)
        amount = 0.0
        shipping_amount = 80.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/add-to-cart.html', 
                      {'carts':cart, 'totalamount':totalamount, 'amount':amount, 'total_amount':total_amount})
            
        else:
            return render(request, 'app/empty_cart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active': 'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user = usr, name = name, locality = locality, city = city, 
                           state = state, zipcode = zipcode)
            reg.save()
            messages.success(request, 'Congratulations !! Your Profile Updates Successfully.')
        return render(request, 'app/profile.html', {'form':form, 'active': 'btn-primary'})    

def plus_cart(request):
    if request.method == 'GET':
        prodt_id = request.GET['prodt_id']
        c = Cart.objects.get(Q(product=prodt_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 80.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
                
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prodt_id = request.GET['prodt_id']
        c = Cart.objects.get(Q(product=prodt_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 80.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
                
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prodt_id = request.GET['prodt_id']
        c = Cart.objects.get(Q(product=prodt_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 80.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
                
        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)
        
@login_required
def address(request):
 addrs = Customer.objects.filter(user = request.user)
 return render(request, 'app/address.html', {'addrs':addrs, 'active': 'btn-primary'})

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user = request.user)
    return render(request, 'app/orders.html', {'order_placed': op})

def PasswordReset(request):
 return render(request, 'app/password_reset.html')

def mobile(request, data = None):
    if data == None:
        mobiles = Product.objects.filter(category= 'M')
    elif data =='Xiaomi' or data =='Samsung' or data =='Realme' or data =='Vivo' or data =='OnePlus' or data =='Itel':
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

@login_required   
def checkout(request):
    user = request.user
    addrs = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 80.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'app/checkout.html', {'addrs':addrs, 
            'cart_items':cart_items ,'totalamount':totalamount})

@login_required   
def payment_done(request):
    user = request.user
    cust_id = request.GET.get('cust_id')
    customer = Customer.objects.get(id=cust_id)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, 
                product = c.product, quantity = c.quantity).save()
        c.delete()
    return redirect("orders")

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

def Camera(request, data = None):
    if data == None:
        cameras = Product.objects.filter(category= 'CM')
    elif data =='Nikon' or data =='Canon' or data =='Sony' or data =='Samsung':
        cameras = Product.objects.filter(category= 'CM').filter(brand = data)
    elif data == 'below':
        cameras = Product.objects.filter(category= 'CM').filter(discounted_price__lt=20000)
    elif data == 'above':
        cameras = Product.objects.filter(category= 'CM').filter(discounted_price__gt=20000)
    return render(request, 'app/camera.html', {'cameras': cameras})

def Watch(request, data = None):
    if data == None:
        watches = Product.objects.filter(category= 'W')
    elif data =='Fastrack' or data =='Tissot' or data =='Titan' or data =='Rolex':
        watches = Product.objects.filter(category= 'W').filter(brand = data)
    elif data == 'below':
        watches = Product.objects.filter(category= 'W').filter(discounted_price__lt=5000)
    elif data == 'above':
        watches = Product.objects.filter(category= 'W').filter(discounted_price__gt=5000)
    return render(request, 'app/watch.html', {'watches': watches})

def Cosmetics(request):
 return render(request, 'app/cosmetics.html')

def Bag(request):
 return render(request, 'app/bag.html')