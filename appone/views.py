# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Order
from .forms import OrderForm
# def web(request):
#     return HttpResponse("This is the website!")
# def appo(request):
#     return HttpResponse("This is the first app!")
# def create(request):
#     return redirect('/stack/')
def home(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.casenum = Order.objects.latest('ordernum').casenum+1
        # print "INSIDE FORM"
        instance.save()
        return HttpResponseRedirect('/appone/order/add/')
    series=Order.objects.all()
    context = {
      "form" : form,
      'series' : series
    }
    return render(request,"home.html",context)
