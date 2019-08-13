from django.shortcuts import render
from django.http import HttpResponse
from .models import Modelclass

def home(request):
    return render(request,'application1/home.html')

def material(request):
    return render(request,'application1/material.html')
def programs(request):
    return render(request,'application1/programs.html')

def registration(request):
    return render(request,'application1/reg.html')

def contact(request):
    return render(request,'application1/contact.html')

def insert(request):
    a=request.POST['t1']
    b=request.POST['t2']
    c=request.POST['t3']
    d=request.POST['t4']
    e=request.POST['t5']
    f=request.POST['t6']
    g=request.POST['t7']
    h=request.POST['t8']
    i=request.POST['t9']
    j=Modelclass(first_name=a,last_name=b,user_name=c,password=d,conform_password=e,email_id=f,mobile_no=g,gender=h,nationality=i)
    j1=j.save()
    if j1:
        return render(request,'application1/login.html')
    else:
        return HttpResponse("<h2>regestration failed</h2>")

def login(request):
    return render(request,'application1/login.html')

def display(request):
    a1=request.POST['t11']
    b1=request.POST['t12']
    c1=Modelclass.objects.filter(user_name=a1,password=b1)
    if c1:
        return render(request,'application1/home.html')
    else:
        return HttpResponse('<h2>login failed</h2>')

def interview(request):
    return render(request,'application1/interview.html')

def basic(request):
    return render(request,'application1/basic python.html')

def advanced(request):
    return render(request,'application1/adv python.html')
