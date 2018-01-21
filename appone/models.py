# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from multiselectfield import MultiSelectField
import django.utils.timezone
from django.core.validators import MaxValueValidator,MinValueValidator
Case_States = (
    ('Saved','Saved'),
    ('Placed', 'Placed'),
    ('Received at Lab','Received at Lab'),
    ('Accepted by Lab','Accepted by Lab'),
    ('Rejected by Lab','Rejected by Lab'),
    ('Order Held','Order Held'),
    ('Processing','Processing'),
    ('Shipped from Lab','Shipped from Lab'),
    ('Arriving Today','Arriving Today'),
    ('Received by Provider','Received by Provider'),
    ('Completed','Completed'),
)
Product_list=["PFM High Noble","PFM Non Precious","Full Gold Crown","Full Cast Semi Precious","Full Cast Non Precious","Crown Fit to Partial","Metal Occlusal","Metal Lingual",
"Zirlux Temporary","Cast Coping","PFM High Noble","PFM Semi Precious","PFM Bridges(Non Precious Alloy)","Emax Bridge","Bruxzir Crown","Zirconia Crown","Lava Crown","Emax Crown","Empress Crown","Zirconia Veneer",
"Bruxzir Bridge 2","Bruxzir Bridge","Zirconia Bridge","Lava Bridge","Emax Bridge","Empress Bridge","Custom Abutment Anterior","Custom Abutment Posterior",
"Custom Zirconia Abutment Anterior","Custom Zirconia Abutment Posterior",
"Conus Abutment","Hybrid Bar"]

def casenum_generate():
    return Order.objects.latest('ordernum').casenum

def provider_generate():
    return Order.objects.latest('ordernum').provider

def location_generate():
    return Order.objects.latest('ordernum').location

class Order(models.Model):
    casenum=models.IntegerField(default=casenum_generate,verbose_name="Case No.",validators=[MinValueValidator(1)])
    ordernum=models.AutoField(primary_key=True,verbose_name="Order No.")
    orderdate=models.DateField(default=django.utils.timezone.now,verbose_name="Order Date")
    provider=models.CharField(max_length=50,default=provider_generate)
    patient=models.CharField(max_length=50)
    product=models.CharField(max_length=50,choices=[(Product_list[x],Product_list[x]) for x in xrange(32)])
    teethnum=MultiSelectField(choices=[(x, x) for x in range(1, 33)],verbose_name="Tooth No.")
    location=models.CharField(max_length=50,default=location_generate)
    expecteddate=models.DateField(verbose_name="Expected Date")
    price=models.IntegerField(null=True)
    status=models.CharField(max_length=50,choices=Case_States,default='saved')
    remarks=models.TextField(max_length=500,null=True,default="No remarks")
    def __unicode__(self):
        return 'Order#' + str(self.ordernum)+' '+str(self.product) +' - '+str(self.status)
    def numberofdaystodelivery(self):
        delta=self.expecteddate-django.utils.timezone.now().date()
        if delta.days<0:
            if self.status!="Completed":
                self.status='Received by Provider'
                self.save()
            return "-"
        elif delta.days==0:
            if self.status!="Completed":
                self.status="Arriving Today"
                self.save()
            return "0"
        else:
            return delta.days
    numberofdaystodelivery.short_description = "Number of days to delivery"
    daystodelivery = property(numberofdaystodelivery)
    def pp(self):
        product=self.product
        x=len(list(str(self.teethnum).split(',')))
        if(product=="PFM High Noble"):
            y= 50*x
        elif(product=="FM Semi Precious"):
            y= 50*x
        elif(product=="PFM Non Precious"):
            y= 50*x
        elif(product=="Full Gold Crown"):
            y= 50*x
        elif(product=="Full Cast Semi Precious"):
            y= 50*x
        elif(product=="Full Cast Non Precious"):
            y= 50*x
        elif(product=="Crown Fit to Partial"):
            y= 50*x
        elif(product=="Metal Occlusal"):
            y= 50*x
        elif(product=="Metal Lingual"):
            y= 50*x
        elif(product=="Zirlux Temporary"):
            y= 50*x
        elif(product=="Cast Coping"):
            y= 50*x
        elif(product=="PFM High Noble"):
            y= 50*x
        elif(product=="PFM Semi Precious"):
            y= 50*x
        elif(product=="PFM Bridges(Non Precious Alloy)"):
            y= 50*x
        elif(product=="Emax Bridge"):
            y= 50*x
        elif(product=="Bruxzir Crown"):
            y= 50*x
        elif(product=="Zirconia Crown"):
            y= 50*x
        elif(product=="Lava Crown"):
            y= 50*x
        elif(product=="Emax Crown"):
            y= 50*x
        elif(product=="Empress Crown"):
            y= 50*x
        elif(product=="Zirconia Veneer"):
            y= 50*x
        elif(product=="Bruxzir Bridge 2"):
            y= 45*x
        elif(product=="Bruxzir Bridge"):
            y= 50*x
        elif(product=="Zirconia Bridge"):
            y= 50*x
        elif(product=="Lava Bridge"):
            y= 50*x
        elif(product=="Emax Bridge"):
            y= 50*x
        elif(product=="Empress Bridge"):
            y= 50*x
        elif(product=="Custom Abutment Anterior"):
            y= 50*x
        elif(product=="Custom Abutment Posterior"):
            y= 50*x
        elif(product=="Custom Zirconia Abutment Posterior"):
            y= 50*x
        elif(product=="Conus Abutment"):
            y= 50*x
        elif(product=="Hybrid Bar"):
            y=  50*x
        else:
            y= 0
        return '$'+str(y)
    price=property(pp)

class Product(models.Model):
    productname = models.CharField(primary_key=True,max_length=500,verbose_name="Product Name")
    cost = models.IntegerField(verbose_name="Cost (in $)")
    def __unicode__(self):
        return 'Product ' + str(self.productname)
