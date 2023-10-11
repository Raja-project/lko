from django.db import models

# Create your models here.
import corpHotelApp.models as cm
class Register(models.Model):

     GENDER_CHOICE=(('male','MALE'),('female','FEmale'))
     uname=models.CharField(max_length=50)
     uemail=models.CharField(max_length=35)
     upass=models.CharField(max_length=12)
     ugender=models.CharField(max_length=8,choices=GENDER_CHOICE,default='male')

class Product(models.Model):
    
      pid=models.BigIntegerField(primary_key=True)
      hid=models.ForeignKey(cm.hotel,on_delete=models.CASCADE)
      hname=models.CharField(max_length=15,default=" ")
      hdesc=models.CharField(max_length=100000,default=" ")
      hrooms=models.IntegerField(default=0)  
      hfacl=models.CharField(max_length=100,default=" ") 
      hrate=models.IntegerField(default=0)
      hprice=models.IntegerField(default=0)
      hdisc=models.IntegerField(default=0)
      img_url=models.ImageField(upload_to='images/',default=" ")
      dt=models.DateTimeField(auto_now_add=True) 
      uemail=models.CharField(max_length=15,default="noemail")