from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from . forms import SignUp
from django.contrib.auth.forms import UserCreationForm
from myapp.models import products,Wishlist,Order
from cart.cart import Cart
from django.contrib import messages
from myapp.forms import ImageHandler
from cart import cart
# Create your views here.

app_name = "myapp"

def index(request):
    data=products.objects.all()
    return render(request,'myapp/index.html',context={
        "data":data
    })

def place_order(request):
    if request.method == "POST":
        full_name=request.POST.get('full_name')
        phone=request.POST.get('phone')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        country=request.POST.get('country')
        zipcode=request.POST.get('zipcode')
        note=request.POST.get('note')
        obj=Order.objects.create(user=request.user,full_name=full_name,phone=phone,address1=address1,address2=address2,city=city,country=country,zipcode=zipcode,note=note)
        x= request.session['cart']
        for key,value in x.items():
            if key == '1':
                product=products.objects.get(pk=value.get('product_id'))
                obj.add_product(product)                
        obj.save()
        return redirect('myapp:index')


@login_required(login_url='/myapp/signin')
def wishlist(request,id):
        product = products.objects.get(pk=id)

        try:
            obj = Wishlist.objects.get(user=request.user)
            obj.add_product(product=product)
        except Wishlist.DoesNotExist:
            obj=Wishlist.objects.create(user=request.user)
            obj.add_product(product)

        
        obj.save()
        return redirect('myapp:index')

@login_required(login_url='/myapp/signin')
def show_wishlist(request):
    user=request.user
    try:
        data = Wishlist.objects.get(user=user).product.all()
        print(data)        
        return render(request,'myapp/shop.html',context={
        "data":data
    })     
    except:
         messages.success(request,"Sorry you haven't any product in wishlist")
         return redirect('myapp:index')


    



@login_required(login_url='/myapp/signin')
def add_to_card(request,id):
    cart=Cart(request)
    product=products.objects.get(id=id)
    cart.add(product=product)
    if 'total' not in request.session:
        request.session['total']=0    
    request.session['total']+=getattr(product,'price')
    messages.success(request,"product added to cart")
    return redirect('myapp:cart')

@login_required
def item_clear(request,id):
    cart=Cart(request)
    product=products.objects.get(id=id)
    request.session['total']-=getattr(product,'price')
    cart.remove(product)
    return redirect('myapp:cart')

@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    request.session['total']=0
    return redirect('myapp:cart')


def signup(request):
    if request.method == 'POST':
        form=SignUp(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            pw=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=pw)
            login(request,user)
            messages.success(request,"user added successfully")
            return redirect('myapp:index')
    else:
        form=SignUp()
    return render(request,'myapp/signup.html',{'form':form}) 

def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"login successful")
            return redirect('myapp:index')
        else:
            return render(request,'myapp/login.html')    
    else:    
        return render(request,'myapp/login.html')
def signout(request):
    logout(request)
    return render(request,'myapp/index.html')  



def cart(request):
    return render(request,'myapp/cart.html')
    
@login_required
def addProduct(request):
    if request.method =='POST':
        imageForm=ImageHandler(request.POST,request.FILES)
        if imageForm.is_valid():
            name=request.POST.get('name')
            brand=request.POST.get('brand')
            description=request.POST.get('description')
            longDescription=request.POST.get('longDescription')
            catageory=request.POST.get('catageory')
            subCatageory=request.POST.get('subCatageory')
            quentity=request.POST.get('quentity')
            image=imageForm.cleaned_data['image']
            price=request.POST.get('price')
            id=request.POST.get('product_id')
            p=products(name=name,price=price,id=id,seller=request.user,description=description,longDescription=longDescription,catageory=catageory,subCatageory=subCatageory,quentity=quentity,rating=0,brand=brand,image=image)
            p.save()
            messages.success(request,"product added successfully")
        return render(request,'myapp/index.html')

    else:
        return render(request,'myapp/addProduct.html')


def checkout(request):
    return render(request,"myapp/checkout.html")
def singleproduct(request,id,catageory):
    data=products.objects.filter(id=id)
    cat=products.objects.filter(catageory=catageory)
    return render(request,'myapp/single-product.html',context={
        "data":data,
        "cat":cat
        })
def shop(request,*args,**kwargs):
    field = kwargs.get('field')
    value = kwargs.get('value')
    if(field=="brand"):
        data=products.objects.filter(brand=value)
    elif(field=="catageory"):   
        data=products.objects.filter(catageory=value)
    else:
        data=products.objects.all()     
    return render(request,'myapp/shop.html',context={
        "data":data
    })        

def search(request):
    if request.method=='POST':
        name=request.POST.get('name')
        data=products.objects.filter(name=name)
        return render(request,'myapp/shop.html',context={
        "data":data
        })
    else:
        return render(request,'myapp/shop.html')

