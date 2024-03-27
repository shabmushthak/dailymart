from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import*
from adminapp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django. db. models.aggregates import Sum

# Create your views here.
def cat_card(request):
    data=Category.objects.all()
    return render(request,'category_card.html',{'data':data})   

def pro_card(request,category):
    if (category=='all'):
        data=product.objects.all()
    else:
        data=product.objects.filter(category=category)
    data2=Category.objects.all()

    return render(request,'product_card.html',{'data':data,'data2':data2})


def cont(request):
    return render(request,'contact.html')




def contactdata(request):
    if request.method=='POST':
        name=request.POST['name']
        number =request.POST['number']
        mail=request.POST['mail']
        data=contact(name=name,number=number,mail=mail)
        data.save()
    return redirect('cat_card')

def contact_table(request,):
    data=contact.objects.all()
    return render(request,'contact_table.html',{'data':data})


def dltcontact(request,id):
    contact.objects.filter(id=id).delete()
    return redirect('contact_table')




def loging(request):
    data=register.objects.all()
    return render(request,'loging.html',{'data':data})


def logingdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if register.objects.filter(username=username,password=password).exists():
           data = register.objects.filter(username=username,password=password).values('id','contact','mail').first()

           request.session['u_id'] = data['id']
           request.session['contact'] = data['contact'] 
           request.session['mail'] = data['mail'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('cat_card') 
        else:
            return render(request,'loging.html',{'msg':'invalid user credentials'})
    else:
        return redirect('loging')

def userlogout(request):
    del request.session['username_u']
    del request.session['password_u']
    del request.session['u_id']
    del request.session['contact']
    del request.session['mail']

    return redirect('loging')



def reg(request):
    return render(request,'register.html')

def registerdata(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        contact=request.POST['contact']
        mail=request.POST['mail']
        data=register(username=username,password=password,contact=contact,mail=mail)
        data.save()
    return redirect('cat_card')   



def register_table(request):
    data=register.objects.all()
    return render(request,'register_table.html',{'data':data})






def dlt1(request,id):
    register.objects.filter(id=id).delete()
    return redirect('register_table')

def home(request):
    data1=product.objects.all()
    data2=Category.objects.all()
    
    return render(request,'main_page.html',{'data1':data1,'data2':data2})

def view_more_pro(request,id):
    data=product.objects.filter(id=id)
    return render(request,'view_more_product.html',{'data':data})

def cart1(request):
    u=request.session.get('u_id')
    data=cart.objects.filter(userid=u,status=0)
    s=cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'s':s})

def checkout1(request):
        u=request.session.get('u_id')
        data=cart.objects.filter(userid=u,status=0)
        return render(request,'checkout.html',{'data1':data})

def about(request):
    return render(request,'about.html')

def cartdata(request,id):
    if request.method=="POST":
        user_id=request.session.get('u_id')
        quantity1=request.POST['quantity']
        total2=request.POST['total']
        data=cart(userid=register.objects.get(id=user_id),productid=product.objects.get(id=id),quantity=quantity1,total=total2)
        data.save()
    return redirect('cart1')

def delete2(request,id):
    cart.objects.filter(id=id).delete()
    return redirect('cart1')


def checkoutdata(request):
    if request.method=="POST":
        user_id=request.session.get('u_id')
        country1=request.POST['country2']
        address1=request.POST['address2']
        city1=request.POST['city2']
        zip1=request.POST['zip2']
        order=cart.objects.filter(userid=user_id,status=0)

        for i in order:
            data = checkout(userid=register.objects.get(id=user_id),cartid=cart.objects.get(id=i.id),country=country1,address=address1,city=city1,postal_zip=zip1)
            data.save()
            cart.objects.filter(id=i.id).update(status=1)
    return redirect('suc')

def suc(request):
    return render(request,'success.html')