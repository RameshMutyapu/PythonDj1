# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def input(request):
    return render(request,"base.html")

def add(request):
    s1=request.GET['t1']
    s2=request.GET['t2']

    i=int(s1)
    j=int(s2)

    k=i+j

    msg="<html><body bgcolor=cyan><h1>Addition of two numbers:" + str(k) + "</h1></body></hmtl>"

    return HttpResponse(msg)