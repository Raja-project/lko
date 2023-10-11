from django.shortcuts import render
import corpHotelApp.models as cm
from django.http import HttpResponse
import random
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage


# Create your views here.
def board(request):
     return render(request,'corpTemp/board.html')

def corp_regis(request):
      if request.method=='POST':
 
         na1=request.POST["na"]
         em1=request.POST['em']
         pa1=request.POST['pwd']
         cid1=random.randint(100000,500000)
        
         print(na1,em1,pa1)
         data=cm.Corporate.objects.create(cid=cid1,cname=na1,cemail=em1,cpass=pa1)
         data.save()
         print("Corporate data Saved succesfully")
            

      return render(request,'corpTemp/corp_register.html')
      
def corp_login(request):
    print("Corp_Login-called")
    if request.method == 'POST':
        em1 = request.POST.get('em')
        pa1 = request.POST.get('pwd')
        print("data from login form =", em1, pa1)      
            
            
        corp = cm.Corporate.objects.get(cemail=em1)

        print(corp.cpass,corp.cid)
        if corp.cpass == pa1:
          print("login success")

          request.session["em"] = corp.cemail
          request.session["pwd"] = True
          return render(request, 'corpTemp/corp_board.html',{'cid':corp.cid})
        else:
                
          return render(request, 'corpTemp/corp_login.html', {'error_message': 'Invalid password'})

       

    return render(request, 'corpTemp/corp_login.html')

def hotelregister(request,cid1=None):
  if request.method=='POST' and request.FILES['upload']:
    hid1=random.randint(100000,50000000)
    hname1=request.POST['hna']
    hdesc1=request.POST['hdesc']
    hrooms1=request.POST['hrooms']
    hfacl1=request.POST['hfacl']
    hrate1=request.POST['hrate']
    hprice1=request.POST['hprice']
    hdisc1=request.POST['hdisc']
    
    #img code
    upload =request.FILES['upload']
    fss = FileSystemStorage()
    file = fss.save(upload.name,upload)
    img_ulr1= fss.url(file)
    print(hid1,hname1,hdesc1,hrooms1,hfacl1,hrate1,hprice1,hdisc1,img_ulr1)
    ob=cm.hotel.objects.create(hid=hid1,cid_id=cid1,hname=hname1,hdesc=hdesc1,hrooms=hrooms1,hfacl=hfacl1,hrate=hrate1,hprice=hprice1,hdisc=hdisc1,img_url=img_ulr1)
    ob.save()
    print("hotel register successfully!")


    
  return render(request,'corpTemp/hotelregis.html')

  


