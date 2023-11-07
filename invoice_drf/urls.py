from django.contrib import admin
from django.urls import path
from api import views

from django.shortcuts import render 

def loadMain(request):
    return render(request,'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoices/', views.getAllInvoices),
    path('', loadMain)
]
