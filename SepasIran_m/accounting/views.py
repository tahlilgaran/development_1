from django.shortcuts import render
from define_trip.models import *
from  accounting.models import *
import datetime

# Create your views here.
def paymentTour(request, tour_id=''):

    number=request.POST.get("number")
    tour= Tour.objects.get(id = tour_id)
    cost=tour.cost
    total_cost=cost * int(number)
    return render(request, "payment_bank.html",{
        'total_cost': total_cost,
        'tour':tour,
    })

def confirmTour(request,tour_id=''):


        tour=Tour.objects.get(id = tour_id)
        user= request.user.userm
        sender= TouristProfile.objects.get(user = user)
        date = datetime.datetime.today()
        amount=300000
            # request.POST.get("total_cost")
        gardesh=tour.gardesh

        info= Trans_info.objects.create(date=date,amount=amount,gardesh=gardesh)
        transaction = Trans_Kind1.objects.create(info=info,sender=sender)

        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'kind':'1',
        })

def ozviyat(request ,username='', password=''):


    return render(request, "payment_bank.html" ,{
        'total_cost':'۳۰۰۰',
    })

