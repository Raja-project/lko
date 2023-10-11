from django.urls import path

import corpHotelApp.views as ca

urlpatterns = [
    path('corpboard/',ca.board),
    path('corp_regis/',ca.corp_regis),
    path('login/',ca.corp_login),
    path('hregis/<int:cid1>',ca.hotelregister),


]
