from django.shortcuts import render,HttpResponse
# from datetime import datetime
from home.models import Contact
# from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        contact = Contact(phone=phone ,email=email)
        contact.save()
        # messages.success(request,"Thank you..")
    return render(request,'contact.html')
 
   