import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from . models import *
from shop.form import customuserform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    product=Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{'product':product})
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out sucessfully")
    return redirect('/')
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user_login=authenticate(request,username=name,password=pwd)
            if user_login is not None:
                login(request,user_login)
                messages.success(request,'logged in Successfully ')
                return redirect("collections")
            else:
                messages.error(request,"Invalid user name or password ")
                return redirect("login")
        return render(request,"shop/login.html")


def addtocart(request):
    if request.headers.get('X-requested-with') == 'XMLHTTpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']

            product_status = Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id, Product_id=product_id):
                    return JsonResponse({'status': 'product already in the cart'}, status=200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user=request.user, Product_id=product_id, product_qty=product_qty)
                        return JsonResponse({'status': 'product added to the cart'})
                    else:
                        return JsonResponse({'status': 'stock not available'})
            else:
                return JsonResponse({'status': 'product not available'})
        else:
            return JsonResponse({'status': 'login to add cart'}, status=200)
    else:
        return JsonResponse({'status': 'invalid access'}, status=200)


def fav_cart(request):
    if request.headers.get('X-requested-with') == 'XMLHTTpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_id = data['pid']
            product_status = Product.objects.get(id=product_id)
            if product_status:
                if fav.objects.filter(user=request.user.id,Product_id=product_id):
                    return JsonResponse({'status':'already in the favourite box'},status=200)
                else:
                    fav.objects.create(user=request.user, Product_id=product_id,)
                    return JsonResponse({'status':'product added to the favourite box'},status=200)
            else:
                return JsonResponse({'status':'product not found !'})
        else:
            return JsonResponse({'status': 'login to add cart !'}, status=200)
    else:
        return JsonResponse({'status': 'invalid access'}, status=200)
def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{'cart':cart})
    else:
        return redirect('/')
def remove_cart(request,cid):
    cart_item=Cart.objects.get(id=cid)
    cart_item.delete()
    return redirect("cart_page")
def fav_page(request):
    if request.user.is_authenticated:
        favourite=fav.objects.filter(user=request.user)
        return render(request,"shop/fav.html",{'fav':favourite})
    else:
        return redirect('/')
def remove_fav(request,fid):
    cart_fav_item=fav.objects.filter(id=fid)
    cart_fav_item.delete()
    return redirect("fav_page")
def register(request):
    form=customuserform()
    if request.method=='POST':
        form=customuserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registeration success you can login now")
            return redirect('login')
    return render(request,"shop/register.html",{'form':form})
def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,'shop/collections.html',{'category':category})
def collectionsview(request,name):
    if (Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,'shop/products/index.html',{'products':products,'category_name':name})
    else:
        messages.warning(request,"no such category found")
        return redirect("collections")
def product_details(request,cname,pname):
    if (Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            product=Product.objects.filter(name=pname,status=0).first()
            return render(request,'shop/products/products.html',{'product':product})
        else:
            messages.error(request,"no product found")
            return redirect('collections')
    else:
        messages.error(request,"no category found") 
        return redirect("collections")
def contact_us(request):
    return render(request,'shop/inc/contact.html')