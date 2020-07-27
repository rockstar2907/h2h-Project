from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from .models import Restaurants,UserDetails,Items,UserOrders,AllOrders,CurrentOrders,Cart

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/users/menu')
        else:
            messages.error(request,'INVALID CREDENTIALS')
            return redirect('users/login')


def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        phno=request.POST['phno']
        address=request.POST['address']
        password=request.POST['password']
        password2=request.POST['password2']
        if password!=password2:
            messages.info(request,'PASSWORDS DID NOT MATCH')
            return render(request,'signup.html')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'oops!!USERNAME TAKEN')
            return redirect('/users/signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'oops!!Email ALREADY IN USE')
            return redirect('/users/signup')
        else:
            user_details=UserDetails(username=username,phno=phno,address=address)
            user=User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
            user.save()
            user_details.save()
            messages.info(request,'USER CREATED')
            return redirect('/users/login')
    else:
        return render(request,'signup.html')

def home(request):
    if request.user.is_authenticated:
        if request.user.username=='h2hadmin':
            return redirect('/users/admin-orders')
        rests=Restaurants.objects.all()
        username=request.user.username
        name=User.objects.get(username=username)
        fname=name.first_name
        return render(request,'menu.html',{'rests':rests,'fname':fname})
    else:
        return redirect('/users/login')

def admin_view(request):
    orders=CurrentOrders.objects.all()
    for i in orders:
        if i.total_amount==0:
            i.delete()
    return render(request,'admin_view.html',{'orders':orders})

def delivered(request,id):
    order=CurrentOrders.objects.get(id=id)
    allorders=AllOrders(username=order.username,phno=order.phno,
        address=order.address,
        rest_name='null',
        items=order.items,
        total_amount=order.total_amount)
    allorders.save()
    order.delete()
    return redirect('/users/admin-orders')

def items(request,rest_name):
    username=request.user.username
    items=Items.objects.filter(rest_name=rest_name)
    if request.method== 'POST':
        d={}
        usn=''
        for i in items:
            id=request.POST[str(i.id)]
            d[id]=request.POST['qty-'+id]
            usn=request.POST['username']
        ids=list(d.keys())
        qty=list(d.values())
        d={}
        for i in range(len(ids)):
            if qty[i]!='0':
                d[ids[i]]=qty[i]
        ids=list(d.keys())
        qty=list(d.values())
        print(ids,qty)
        for i in range(len(ids)):
            id=ids[i]
            quantity=qty[i]
            price=Items.objects.get(id=id)
            item_name=price.item_name
            total_price=price.price*int(quantity)
            check_count=Cart.objects.filter(item_id=id).count()
            if check_count>0:
                check=Cart.objects.get(item_id=id)
                check.qty+=int(quantity)
                check.price+=total_price
                check.save()
            else:
                cart=Cart(username=username,qty=quantity,item_id=price,rest_name=rest_name,price=total_price,item_name=item_name)
                cart.save()
                print(username)
        return redirect('/users/cart')
    return render(request,'items.html',{'items':items,'rest_name':rest_name,'username':username})

def logout(request):
    auth.logout(request)
    return redirect('/')

def cart(request):
    username=request.user.username
    if request.user.is_authenticated:
        if request.method=='POST':
            UserOrders.objects.filter(username=username).delete()
            d={}
            cart=Cart.objects.filter(username=username)
            for i in cart:
                id=request.POST[str(i.item_id.id)]
                qty=request.POST['qty-'+id]
                d[id]=qty
            ids=list(d.keys())
            qty=list(d.values())
            d={}
            for i in range(len(ids)):
                if qty[i]!='0':
                    d[ids[i]]=qty[i]
            ids=list(d.keys())
            qty=list(d.values())
            for i in range(len(ids)):
                id=ids[i]
                quantity=qty[i]
                username=request.user.username
                price=Items.objects.get(id=id)
                rest_name=price.rest_name.rest_name
                item_name=price.item_name
                total_price=price.price*int(quantity)
                user_order=UserOrders(username=username,item_id=id,qty=quantity,price=total_price,item_name=item_name,rest_name=rest_name)
                user_order.save()
            return redirect('/users/order')
        cart=Cart.objects.filter(username=username)
        items=Items.objects.all()
        total=0
        for i in cart:
            total+=i.price
        return render(request,'cart.html',{'cart':cart,'total':total,'items':items})
    else:
        return redirect('/users/login')    

def order(request):
    username=request.user.username
    order=UserOrders.objects.filter(username=username)
    items=Items.objects.all()
    total=0
    for i in order:
        total+=i.price
    return render(request,'checkout.html',{'order':order,'items':items,'total':total})

def recieved(request):
    return render(request,'order_recieved.html')
def checkout(request):
    username=request.user.username
    order=UserOrders.objects.filter(username=username)
    user_det=UserDetails.objects.get(username=username)
    phno=user_det.phno
    address=user_det.address
    total=0
    items=''
    for i in order:
        total+=i.price
        items+=i.item_name
        items+='x'
        items+=str(i.qty)
        items+='(From '
        items+=i.rest_name
        items+=')||'
    current=CurrentOrders(username=username,phno=phno,address=address,total_amount=total,items=items,rest_name='null')
    current.save()
    order.delete()
    Cart.objects.filter(username=username).delete()
    return render(request,'order_recieved.html')

def cancel(request):
    username=request.user.username
    cart=Cart.objects.filter(username=username).delete()
    order=UserOrders.objects.filter(username=username).delete()
    return redirect('/users/menu')

def account(request):
    username=request.user.username
    user_det=UserDetails.objects.filter(username=username)
    name_obj=User.objects.get(username=username)
    name=name_obj.first_name+' '+name_obj.last_name
    return render(request,'account.html',{'user_det':user_det,'name':name})

def edit_phno(request):
    if request.method=='POST':
        username=request.user.username
        user_det=UserDetails.objects.get(username=username)
        new_phno=request.POST['new_phno']
        user_det.phno=new_phno
        user_det.save()
        return redirect('/users/account')
    return render(request,'edit_phno.html')

def edit_address(request):
    if request.method=='POST':
        username=request.user.username
        user_det=UserDetails.objects.get(username=username)
        new_address=request.POST['new_address']
        user_det.address=new_address
        user_det.save()
        return redirect('/users/account')
    return render(request,'edit_address.html')

def allorders(request):
    username=request.user.username
    current_orders=CurrentOrders.objects.filter(username=username)
    all_orders=AllOrders.objects.filter(username=username)
    return render(request,'allorders.html',{'current_orders':current_orders,'all_orders':all_orders})