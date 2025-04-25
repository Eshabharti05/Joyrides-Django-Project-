
    
from django.db import models
import datetime
import os

# Create your models here.
class Banner(models.Model):
    image=models.ImageField(upload_to='banner/')
class Register(models.Model):
    username=models.CharField(null=False,max_length=255,)
    mobile_no=models.IntegerField(null=False)
    email=models.CharField(max_length=15)
    password=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.username}"
    
def filepath(request,filename):
    old_filename=filename
    timenow=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (timenow,old_filename)
    return os.path.join('uploads/',filename)
    
class Product(models.Model):
    prod_img=models.ImageField(upload_to=filepath,null=True,blank=True)
    prod_name=models.CharField(null=False,max_length=255)
    price=models.IntegerField(null=False)
    mileage=models.CharField(null=False,max_length=255)
    color=models.CharField(null=False,max_length=255)
    cc=models.CharField(null=False,max_length=255)

    def __str__(self):
        return f"{self.prod_name}"

class Order_list(models.Model):
    username=models.CharField(null=False,max_length=255,)
    mobile_no=models.IntegerField(null=False)
    email=models.CharField(max_length=15)
    prod_img=models.ImageField(upload_to=filepath,null=True,blank=True)
    prod_name=models.CharField(null=False,max_length=255)
    price=models.IntegerField(null=False)
    aadhar=models.IntegerField(null=False)
    driving_license=models.CharField(null=False,max_length=255)
    pan_card=models.CharField(null=False,max_length=255)
    address=models.CharField(null=False,max_length=255)

    def __str__(self):
        return f"{self.username + self.prod_name }"
    
class Adminregister(models.Model):
    username=models.CharField(null=False,max_length=255,)
    password=models.CharField(max_length=255)