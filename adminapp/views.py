from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import*
from userapp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


def add_category(request):
    return render(request,'add_category.html')



def categorydata(request):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
       
        image=request.FILES['image']
        data=Category(name=name,description=description,image=image,)
        data.save()
    return redirect('table_category')


def table_category(request):
    data=Category.objects.all()
    return render(request,'table_category.html',{'data':data})


def update(request,id):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']

        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file =Category .objects.get(id=id).image
        Category.objects.filter(id=id).update(name=name, description= description,image=file)
        return redirect('table_category')
     
def edit(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'edit_category.html',{'data':data})


def dlt(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('table_category')


def add_product(request):
    data=Category.objects.all()
    return render(request,'add_product.html',{'data3':data})

def table_product(request):
    data=product.objects.all()
    return render(request,'table_product.html',{'data':data})



def productdata(request):
    if request.method=='POST':
        name=request.POST['name']
        category=request.POST['category']
        price=request.POST['price']
        description=request.POST['description']
        
        image=request.FILES['image']
        data=product(name=name,category=category,image=image, price=price,description=description)
        data.save()
    return redirect('table_product')

def updateproduct(request,id):
    if request.method=='POST':
        name=request.POST['name']
        category=request.POST['category']
        price=request.POST['price']
        

        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file =product .objects.get(id=id).image
        product.objects.filter(id=id).update(name=name,category=category,price = price,image=file)
        return redirect('table_product')
     
def editpro(request,id):
    data1=Category.objects.all()
    data=product.objects.filter(id=id)
    return render(request,'edit_product.html',{'data':data,'data3':data1})


def dltpro(request,id):
    product.objects.filter(id=id).delete()
    return redirect('table_product')


def admin_home(request):
     totalcategory=Category.objects.all().count()
     totalproduct=product.objects.all().count()
     totalregister=register.objects.all().count()
     totalcontact=contact.objects.all().count()
     
     
     return render(request,'admin_page.html',{'totalcategory':totalcategory,'totalproduct':totalproduct,'totalregister':totalregister,'totalcontact':totalcontact})

def order_table(request):
    data=checkout.objects.all()
    return render(request,'order_table.html',{'data':data})

def dltorder(request,id):
    checkout.objects.filter(id=id).delete()
    return redirect('order_table')