from django.db import models


# Create your models here.
class Corporate(models.Model):

     cid=models.BigIntegerField(primary_key=True,)
     cname=models.CharField(max_length=50)     
     cemail=models.CharField(max_length=35)
     cpass=models.CharField(max_length=12)
     cstatus=models.CharField(max_length=7,default="True")
     cdt=models.DateTimeField(auto_now_add=True)
     
class hotel(models.Model):
      hid=models.BigIntegerField(primary_key=True)
      cid=models.ForeignKey(Corporate,on_delete=models.CASCADE)
      hname=models.CharField(max_length=15,default=" ")
      hdesc=models.CharField(max_length=100000,default=" ")
      hrooms=models.IntegerField(default=0)  
      hfacl=models.CharField(max_length=100,default=" ") 
      hrate=models.IntegerField(default=0)
      hprice=models.IntegerField(default=0)
      hdisc=models.IntegerField(default=0)
      img_url=models.ImageField(upload_to='images/',default=" ")


