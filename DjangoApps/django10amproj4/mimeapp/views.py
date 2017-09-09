# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

data="<table><tr><th>eid></th><th>ename</th><th>esal</th></tr><tr><td>1001</td><td>scott</td>2000</td><td>1002</td><td>blake</td>3000</td><td>1001</td><td>miller</td>4000</td></tr></table>"

def htmlview(request):
     return
     HttpResponse(data,content_type='text/html')

def excelview(request):
     return
     HttpResponse(data,content_type='application/vnd.ms-excel')
def pdfview(request):
     return
     HttpResponse(data,content_type='application/pdf')