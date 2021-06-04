from django.db.models.aggregates import Count
from .models import  mychart
from django.db import models
from django.shortcuts import render
from django.db.models import Sum

def index(Request):
    data=mychart.objects.all()
    items = mychart.objects.aggregate(Sum('counteryseles'))
    mytotal= sum(data.values_list('counteryseles', flat=True))
    mytotal1= sum(data.values_list('counterypepol', flat=True))

#annotate(Sum('counteryseles'))

    countsels=mychart.objects.all().count()
    total = 0
    for cred in data.all():
        total += cred.counteryseles

    context={
        'data':data,
        'p':'wow',
        'countsels':countsels,
        'total':total,
        'totalcount':countsels,
        'items':items,
        'mytotal':mytotal,
        'mytotal1':mytotal1

    }
    return render(Request,'index.html',context)




def cotegoery(Request):
    return render(Request ,'index.html')



def login(Request):
    return render(Request,'pages/login.html')


def chart(Request):
    data=mychart.objects.all()
    
    context={
        'data':data,
       

    }



    return render(Request,'pages/chart.html',context)


def singup(request):
 
    return render(request,'pages/singup.html')

# Create your views here.
