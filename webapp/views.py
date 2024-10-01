from django.shortcuts import render,redirect
from webapp.models import contactdb,signindb,cartdb,orderdb
from textileapp.models import category,Products
from django.contrib import messages
import razorpay
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def home_page(request):
    cat= category.objects.all()
    return render(request,'home.html',{'category':cat})
def about_us(request):
    cat = category.objects.all()
    return render(request,'About us.html',{'category':cat})
def contact(request):
    cat = category.objects.all()
    return render(request,'contact.html',{'category':cat})
def save_contact(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('message')
        obj = contactdb( name=a, email=b, message=c)
        obj.save()
        return redirect(contact)
def all_product(request):
    cat = category.objects.all()
    products=Products.objects.all()
    return render(request,'all_product.html',{'products':products,'category':cat})
def single_product(request,pro_id):
    cat = category.objects.all()
    product=Products.objects.get(id=pro_id)
    return render(request,'single_product.html',{'product':product,'category':cat})
def filtered_product(request,cat_id):
    cat = category.objects.all()
    data=Products.objects.filter(category_name=cat_id)
    return render(request,'filtered_product.html',{'data':data,'category':cat})
def login_user(request):
    return render(request,'login_page.html')
def sign_user(request):
    return render(request,'sign_in.html')


def save_user(request):
    if request.method=="POST":
        a = request.POST.get('username')
        b = request.POST.get('email')
        c = request.POST.get('p1')

        obj=signindb(username=a,email=b,password=c)
        obj.save()
        return redirect(login_user)
def user_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if signindb.objects.filter(username=un,password=pwd):
            request.session['username']=un
            request.session['password']=pwd
            return redirect(home_page)
        else:
            return redirect(login_user)


def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_user)

def save_cart(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('quantity')
        c = request.POST.get('price')
        d = request.POST.get('totalprice')
        e= request.POST.get('username')
        obj=cartdb(product_name=a,quantity=b,price=c,total_price=d,user_name=e)
        obj.save()
        messages.success(request,"Added to cart")
        return redirect(home_page)

def cart_page(request):
    cat = category.objects.all()
    data=cartdb.objects.filter(user_name=request.session['username'])
    sub_total=0
    for i in data:
        sub_total += i.total_price
        if sub_total>3000:
            shipping=200
        else:
            shipping=300
        total=sub_total+shipping

    return render(request,'cart.html',{'data':data,'sub_total':sub_total,'shipping':shipping,
                                       'total':total,'category':cat})
def delete_cart(request,delid):
    x=cartdb.objects.filter(id=delid)
    x.delete()
    messages.error(request,"item deleted")
    return redirect(cart_page)
def check_out(request):
    data = cartdb.objects.filter(user_name=request.session['username'])
    sub_total = 0
    for i in data:
        sub_total += i.total_price
        if sub_total > 3000:
            shipping = 200
        else:
            shipping = 300
        total = sub_total + shipping
    return render(request,'check_out.html',{'data':data
        ,'sub_total':sub_total,'shipping':shipping,'total':total})

def payment_page(request):
    customer = orderdb.objects.order_by('-id').first()

    payy = customer.total_price
    amount = int(payy*100)
    payy_str = str(amount)

    for i in payy_str:
        print(i)

    if request.method == "POST":
        order_currency='INR'
        client = razorpay.Client(auth=('rzp_test_f9tvF898lXtAoP', '33gATP6Hen3bdhgYhRI29SGN'))
        payment = client.order.create({'amount':amount,'currency':order_currency})

    return render(request,'payment.html',{'customer':customer,'payy_str':payy_str})
def save_order(request):
    if request.method=="POST":
        a = request.POST.get('firstname')
        b = request.POST.get('lastname')
        c = request.POST.get('country')
        d = request.POST.get('address')
        e = request.POST.get('city')
        f = request.POST.get('state')
        g = request.POST.get('postcode')
        h = request.POST.get('phone')
        i = request.POST.get('email')
        j = request.POST.get('ordernotes')
        k = request.POST.get('username')
        l = request.POST.get('totalprice')
        obj=orderdb(first_name=a,last_name=b,country=c,address=d,city=e,state=f,
                    postcode=g,phone=h,email=i,order_notes=j,total_price=l,user_name=k)
        obj.save()
        return redirect(payment_page)
