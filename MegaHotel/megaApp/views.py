from django.shortcuts import render
from megaApp.models import Register,Product
import corpHotelApp.models as cm
import random

# Create your views here.
def index(request):   

     ob=cm.hotel.objects.all()[:6];
     print("all-hotel",ob)
     return render (request,'megaTemp/index.html',{'hotels':ob})

     
def board(request):
     return render (request,'megaTemp/board.html')

def Register1(request):

     if request.method=='POST':

         nam1=request.POST["na"]
         em1=request.POST['em']
         pa1=request.POST['pwd']
         gen1=request.POST['gen']
         print(nam1,em1,pa1,gen1)
         data=Register(uname=nam1,uemail=em1,upass=pa1,ugender=gen1)
         data.save()
         print("Data Saved Successfuly")    
     return render(request,'megaTemp/register.html')     


def login(request):
     print("Cust_Login-called")

     if request.method=='POST':
          em1=request.POST['em']
          pa1=request.POST['pwd']
          print("data from login form =", em1, pa1)      
            
            
          cust = Register.objects.get(uemail=em1)

        
          if cust.upass == pa1:
            print("login success")

            request.session["em"] = cust.uemail
            request.session["pwd"] = True

            return render(request, 'custTemp/cust_board.html',{'em':cust.uemail})
          else:
                
            return render(request, 'megaTemp/login.html', {'error_message': 'Invalid password'})          
     
     return render(request, 'megaTemp/login.html')  

def all_corporates(request):
     ob=cm.hotel.objects.all();
     print(ob)
     return render (request,'megaTemp/all_corporates.html',{'hotels':ob})


def hotelDetail(request,hid1=None):
     print(hid1)
     request.session["em"] 
     request.session["pwd"] 
     #if  request.session["em"] :
     if request.method=='POST':
               #hname1=request.POST['hname']
               hid1=request.POST['hid']
               
               rooms=request.POST['rooms']
               print(hid1,rooms)
               pid1=random.randint(100000,50000000)
               ob1=cm.hotel.objects.get(hid=int(hid1))
               print("Booke-hotel",ob1.hname)
               tp=(ob1.hprice*int(rooms))
               tp1=(tp*ob1.hdisc/100)
               fp=(tp-tp1)
               print("TotalPayble=",fp)
               pro=Product(pid=pid1,hname=ob1.hname,hdesc=ob1.hdesc,hfacl=ob1.hfacl,hrooms=rooms,hrate=ob1.hrate,hdisc=ob1.hdisc,hprice=fp,img_url=ob1.img_url,hid_id=ob1.hid,uemail=request.session["em"] )
               pro.save()

          

     if hid1:
         
          ob=cm.hotel.objects.get(hid=hid1)
          print("all-hotel",ob)
          return render (request,'megaTemp/hotel-details.html',{'hd':ob})
    
     
     return render (request,'megaTemp/hotel-details.html')

def mHotels(request):
      ob=cm.hotel.objects.all();
      print("all-hotel",ob)

     
      return render (request,'megaTemp/more-hotels.html',{'hotels':ob})


def booked_hotels(request,email1=None):
     ob=Product.objects.all()
     print("all-booked-hotel",ob)
     
     return render (request,'megaTemp/cust_history.html',{'hotels':ob})


def contact(request):
     return render(request,'megaTemp/contact_us.html')     
    