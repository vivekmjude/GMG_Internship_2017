from .models import Order
import datetime
m1=Order.objects.order_by('-expecteddate')[0].expecteddate
m1c=Order.objects.filter(expecteddate__month=m1.month).count()
m1=m1.strftime("%B")
print m1,m1c

m2=Order.objects.order_by('-expecteddate')[0+m1c].expecteddate
m2c=Order.objects.filter(expecteddate__month=m2.month).count()
m2=m2.strftime("%B")

m3=Order.objects.order_by('-expecteddate')[0+m1c+m2c].expecteddate
m3c=Order.objects.filter(expecteddate__month=m3.month).count()
m3=m3.strftime("%B")

m4=Order.objects.order_by('-expecteddate')[0+m1c+m2c+m3c].expecteddate
m4c=Order.objects.filter(expecteddate__month=m4.month).count()
m4=m4.strftime("%B")

m5=Order.objects.order_by('-expecteddate')[0+m1c+m2c+m3c+m4c].expecteddate
m5c=Order.objects.filter(expecteddate__month=m5.month).count()
m5=m5.strftime("%B")

m6=Order.objects.order_by('-expecteddate')[0+m1c+m2c+m3c+m4c+m5c].expecteddate
m6c=Order.objects.filter(expecteddate__month=m6.month).count()
m6=m6.strftime("%B")

def month1(request):
    return {'month1': str(m1)}
def month2(request):
    return {'month2': str(m2)}
def month3(request):
    return {'month3': str(m3)}
def month4(request):
    return {'month4': str(m4)}
def month5(request):
    return {'month5': str(m5)}
def month6(request):
    return {'month6': str(m6)}

def month1c(request):
    return {'month1c': str(m1c)}
def month2c(request):
    return {'month2c': str(m2c)}
def month3c(request):
    return {'month3c': str(m3c)}
def month4c(request):
    return {'month4c': str(m4c)}
def month5c(request):
    return {'month5c': str(m5c)}
def month6c(request):
    return {'month6c': str(m6c)}
