from django.shortcuts import render,redirect
from textileapp.models import category,Products
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from webapp.models import contactdb
from django.contrib import messages
# Create your views here.
def index_page(request):
    return render(request,'index.html')
def add_categories(request):
    return render(request,'addcategories.html')
def save_category(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b = request.POST.get('description')
        c = request.FILES['image']

        obj=category(name=a,description=b,image=c)
        obj.save()
        messages.success(request,"successfully created")

        return redirect(add_categories)
def display_category(request):
    categories=category.objects.all()
    return render(request,'display_category.html',{'categories':categories})
def edit_categ(request,cat_id):
    data = category.objects.get(id=cat_id)
    return render(request,'edit_reg.html',{'data':data})
def update_reg(request,data_id):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=category.objects.get(id=data_id).image
        category.objects.filter(id=data_id).update(name=name,description=address,image=file)
        return redirect(display_category)
def add_product(request):
    categry=category.objects.all()
    return render(request,'addproduct.html',{'category':categry})
def view_product(request):
    products = Products.objects.all()
    return render(request, 'View product.html', {'products': products})

def save_products(request):
    if request.method=="POST":
        cat = request.POST.get('category')
        a=request.POST.get('pro_name')
        b = request.POST.get('pro_brand')
        c = request.POST.get('pro_price')
        d= request.POST.get('description')
        e = request.FILES['image1']
        f = request.FILES['image2']
        g = request.FILES['image3']

        obj=Products(category_name=cat,product_name=a,brand=b,price=c,description=d,image1=e,image2=f,image3=g)
        obj.save()
        return redirect(add_product)
def edit_products(request,product_id):
    data = Products.objects.get(id=product_id)
    cat=category.objects.all()
    return render(request, 'edit_product.html', {'data': data, 'cat':  cat})

def delete_product(request,product_id):
    x=Products.objects.filter(id=product_id)
    x.delete()
    return redirect(view_product)
def update_product(request,data_id):
    if request.method=="POST":
        a=request.POST.get('category')
        b=request.POST.get('pro_name')
        c = request.POST.get('pro_brand')
        d = request.POST.get('pro_price')
        e= request.POST.get('description')
        try:
            img1 = request.FILES['image1']
            fs = FileSystemStorage()
            file1 = fs.save(img1.name,img1)
        except MultiValueDictKeyError:
            file1=Products.objects.get(id=data_id).image1
        try:
            img2 = request.FILES['image2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2 = Products.objects.get(id=data_id).image2
        try:
            img3 = request.FILES['image3']
            fs = FileSystemStorage()
            file3 = fs.save(img2.name, img3)
        except MultiValueDictKeyError:
            file3 = Products.objects.get(id=data_id).image3
        Products.objects.filter(id=data_id).update(category_name=a,product_name=b,brand=c,price=d,
                                                   description=e,image1=file1,image2=file2,image3=file3)
        return redirect(view_product)
def admin_page(request):
    return render(request,'adminlogin.html')
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request, x)
                request.session["username"] = un
                request.session["password"] = pwd
                messages.success(request,"login succesfull")
                return redirect(index_page)
            else:
                messages.warning(request,"")
                return redirect(admin_page)
        else:
            return redirect(admin_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_page)
def view_contact(request):
    contact=contactdb.objects.all()
    return render(request, 'view_contact.html', {'contact': contact})
def delete_contact(request,contact_id):
    x=contactdb.objects.filter(id=contact_id)
    x.delete()
    return redirect(view_contact)

