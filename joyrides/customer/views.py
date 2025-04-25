from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'home.html',{'title': 'Home'})
def menu(request):
    prod_data=Product.objects.all()
    return render(request, 'menu.html',{'title': 'Menu','data': prod_data})
def login(request):
    if request.method=='POST':
        password=request.POST['password']
        email=request.POST['email']
        data=Register.objects.filter(password=password,email=email).first()
        if data is not None:
            request.session['email']=email
            messages.add_message(request,messages.SUCCESS,'Successfully Login!!')
            return redirect('home')
        else:
            messages.add_message(request,messages.SUCCESS,'Please enter correct credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html',{'title': 'login'})
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        mobile_no=request.POST['mobile_no']
        old_data=Register.objects.filter(username=username,email=email).first()
        if old_data is not None:
            messages.add_message(request,messages.SUCCESS,'You have already been logged in! Enter correct credentials!')
            return redirect('signup')
        else:
            data=Register.objects.create(username=username,password=password,mobile_no=mobile_no,email=email)
            messages.add_message(request,messages.SUCCESS,'Successfully Registered!!')
            return redirect('login')
            
    else:
        return render(request, 'signup.html',{'title': 'signup'})
def about(request):
    return render(request, 'about.html',{'title': 'about'})
def contact(request):
    return render(request, 'contact.html',{'title': 'contact'})
def logout(request):
    del request.session['email']
    messages.add_message(request, messages.SUCCESS, "Logout Successfully!!")
    return redirect('home')
def bicycle(request):
    return render(request, 'bicycle.html',{'title': 'bicycle'})
def bikes(request):
    return render(request, 'bikes.html',{'title': 'bikes'})
def scooter(request):
    return render(request, 'scooter.html',{'title': 'scooter'})
def splendor(request):
    return render(request, 'splendor.html',{'title': 'splendor'})


    
    


def user_list(request):
    # data=Register.objects.all()
    # data=Register.objects.filter(mobile_no=7903493441).values()
    # data=Register.objects.get(id=1)
    data=Register.objects.all()
    return render(request,'admin/user.html',{'title':'User List','data':data})
def delete_user(request,id):
    data=Register.objects.get(id=id)
    data.delete()
    return redirect('user_list')


def editUser(request,id):
    # here id comes with user.html {url 'edit_user' i.id} of particular user
    # and that id of that user is checked in Register
    # that particular register or user details will go to edituser form

    data=Register.objects.filter(id=id).first()
    return render(request,'edit_user.html',{'data':data})


def update_user(request):
    # for updating in that particular user details again that id is stored in the form
    # and then fetched here by POST
    
    name=request.POST['username']
    mobile_no=request.POST['mobile_no'] 
    email=request.POST['email'] 
    password=request.POST['password'] 
    editid=request.POST['editid'] 
    data=Register.objects.get(id=editid)
    data.username=name
    data.mobile_no=mobile_no
    data.email=email
    data.password=password
    data.save()
    messages.add_message(request,messages.SUCCESS,'Successfully Updated!!')
    return redirect('user_list')



def prod_detail(request):
    prod_data=Product.objects.all()
    return render(request, 'admin/prod_detail.html',{'title': 'Product Details','data':prod_data})
def order_list(request):
    order_data=Order_list.objects.all()
    return render(request, 'admin/order_list.html',{'title': 'Order_Details','data':order_data})

def add_prod(request):
    if request.method=='POST':
        prod_name=request.POST['prod_name']
        price=request.POST['price']
        mileage=request.POST['mileage']
        color=request.POST['color']
        cc=request.POST['cc']
        
        if len(request.FILES)!=0:
            prod_img=request.FILES['prod_img']

        prod_data=Product.objects.create(prod_name=prod_name,price=price,mileage=mileage,color=color,cc=cc,prod_img=prod_img)
        messages.add_message(request,messages.SUCCESS,'Successfully Added!!')
        return redirect('prod_detail')
    else:
        return render(request, 'admin/add_prod.html',{'title': 'Add Product'})
    
def deleteProd(request,id):
    prod_data=Product.objects.get(id=id)
    prod_data.delete()
    return redirect('prod_detail')
def editProd(request,id):
    prod_data=Product.objects.filter(id=id).first()
    return render(request,'admin/edit_prod.html',{'data':prod_data})
def updateProd(request):
    prod_name=request.POST['prod_name']
    price=request.POST['price']
    mileage=request.POST['mileage']
    color=request.POST['color']
    cc=request.POST['cc']
        
    if len(request.FILES)!=0:
        prod_img=request.FILES['prod_img']
    editidprod=request.POST['editid'] 
    prod_data=Product.objects.get(id=editidprod)
    prod_data.prod_name=prod_name
    prod_data.price=price
    prod_data.mileage=mileage
    prod_data.color=color
    prod_data.prod_img=prod_img
    prod_data.save()
    messages.add_message(request,messages.SUCCESS,'Successfully Updated!!')
    return redirect('prod_detail')

def viewdetails(request,id):
    if request.session.is_empty():
        return redirect('signup')
    else:
        prod_data=Product.objects.filter(id=id).first()
        return render(request,'viewdetails.html',{'prod_data':prod_data})
        
def form(request,id):
    register_data=Register.objects.filter(email=request.session['email']).first()
    prod_data=Product.objects.filter(id=id).first()
    return render(request,'form.html',{'prod_data':prod_data,'register_data':register_data})

def booking(request):
     if request.method=='POST':
        register_data=Register.objects.filter(email=request.session['email']).first()
        bike_id=request.POST['bike_id']
        prod_data=Product.objects.filter(id=bike_id).first()

        username=register_data.username
        mobile_no=register_data.mobile_no
        email=register_data.email
        prod_img=prod_data.prod_img
        prod_name=prod_data.prod_name
        price=prod_data.price
        aadhar=request.POST['aadhar']
        driving=request.POST['driving_license']
        pan_card=request.POST['pan_card']
        address=request.POST['address']
        order_data=Order_list.objects.create(username=username,mobile_no=mobile_no,
        email=email,prod_img=prod_img,prod_name=prod_name,price=price,
        aadhar=aadhar,driving_license=driving,pan_card=pan_card,address=address)
        messages.add_message(request, messages.SUCCESS, "Order Booking Successfully!!")
        return redirect('home')
     else:
        return render(request, 'form.html',{'title': 'form'})
def adminlogin(request):
    if request.method=='POST':
        password=request.POST['password']
        username=request.POST['username']
        data=Adminregister.objects.filter(password=password,username=username).first()
        if data is not None:
            request.session['username']=username
            messages.add_message(request,messages.SUCCESS,'Welcome Admin!!')
            return redirect('user_list')
        else:
            messages.add_message(request,messages.SUCCESS,'Please enter correct credentials!')
            return redirect('adminlogin')
    else:
        return render(request, 'admin/adminlogin.html',{'title': 'login'})