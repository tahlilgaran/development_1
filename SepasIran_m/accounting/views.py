from django.shortcuts import render
from define_trip.models import *
from  accounting.models import *
from datetime import datetime

# Create your views here.
def paymentTour(request, tour_id='', number=''):
    tour= Tour.objects.get(id = tour_id)
    cost=tour.entire_cost
    total_cost=cost * number
    return render(request, "payment_bank.html",{
        'total_cost': total_cost
    })

def confirmTour(request,tour_id=''):

    if request.method == 'POST':
        tour=Tour.objects.get(id=tour_id)
        #todo : making transaction object kind1
        sender= request.POST.get("username","");
        date = datetime.now()
        ammount=request.POST.get("total_cost","")
        gardesh=tour.gardesh
        info=models.Trans_info(date=date, ammount=ammount, gardesh= gardesh)

        transaction = models.Trans_kind1(info=info , sender=sender)
        transaction.save()
        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'kind':'1',
        })

def cancel(request ,kind=''):

    if kind == 'service':
        return render(request , "canceling.html", {'kind':kind})
    elif kind == 'tour':
        return render(request, "canceling.html" , {'kind':kind})

    return render(request, "canceling.html" , {'kind':kind})

