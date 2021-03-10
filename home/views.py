from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User, sellnewcar,sellcar, finreq

def home(request):
    count=User.objects.all().count()
    oldcar=sellcar.objects.all().count()
    newcar=sellnewcar.objects.all().count()
    finr=finreq.objects.all().count()
    context={"count": count,"oldcar":oldcar,"newcar":newcar,"finr":finr}
    return render(request,'home.html',context)

def login(request):
    return render(request,'login.html')