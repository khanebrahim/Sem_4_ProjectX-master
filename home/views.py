from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
         "variable":"this is sent"
    }
    # messages.success(request, 'this is a success message')
    return render(request, 'index.html')
def home(request):
    return render(request, 'index.html')
def worksheet(request):
    return render(request, 'worksheet.html')
#     # return HttpResponse("this is aboutpage")
# def services(request):
#     return render(request, 'services.html')
#     # return HttpResponse("this is service page")
def easyPproject(request):
    return render(request,'easyPproject.html')
def intmPproject(request):
    return render(request,'intmPproject.html')
def advPproject(request):
    return render(request,'advPproject.html')
def easyCPproject(request):
    return render(request,'easyCPproject.html')
def intmCPproject(request):
    return render(request,'intmCPproject.html')
def advCPproject(request):
    return render(request,'advCPproject.html')
def easyCproject(request):
    return render(request,'easyCproject.html')
def intmCproject(request):
    return render(request,'intmCproject.html')
def advCproject(request):
    return render(request,'advCproject.html')
def easyJproject(request):
    return render(request,'easyJproject.html')
def intmJproject(request):
    return render(request,'intmJproject.html')
def advJproject(request):
    return render(request,'advJproject.html')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        C1 = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        C1.save()
        messages.success(request, 'Profile Successfuly Saved')
    return render(request,'contact.html')

