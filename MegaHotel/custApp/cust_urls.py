from django.urls import path

import custApp.views as mv

urlpatterns = [
    path('custboard/',mv.board),
   
]
