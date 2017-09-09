# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render
from .models import Product
from django.http import HttpResponse

def input(request):
    return  render(request,'input.html')

def insert(request):
    pid1=int(request.GET[t1])
    pname1=request.GET(t2)
    pcost1=float(request.GET[t3])
    pmfd1=request.GET(t4)
    pexpdt1=request.GET(t5)

f=Product(pid=pid1, pname=pname1, pcost=post1, pmfd=pmfd1,pexpdt=pexpdt1)

f.save
return HttpResponse("Data inserted successfully")

def display(request):
    recs=Product.object.all()
    return render(request,'display.html')
