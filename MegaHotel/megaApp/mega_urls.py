from django.urls import path

import megaApp.views as mv

urlpatterns = [
  
    path('main/',mv.board),
    path('regis/',mv.Register1),
    path('login/',mv.login),
    path('all-corp/',mv.all_corporates),
    path('hdetail/<int:hid1>/',mv.hotelDetail),
    path('mhotel/',mv.mHotels),
    path('booked/<slug:email1>/',mv.booked_hotels),
    path('contact_us/',mv.contact),
    
]
