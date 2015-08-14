from django.shortcuts import render
from define_trip.models import *
from accounting.models import *
from datetime import datetime
from buy_cancel.models import *
from buy_cancel.forms import numberForm,peopleForm,hotelForm,tableForm

# Create your views here.
def paymentTour(request, tour_id=''):

    number=request.POST.get("number")
    tour= Tour.objects.get(id = tour_id)
    cost=tour.cost
    total_cost=cost * int(number)
    gardesh = tour.gardesh
    first_name = request.POST.getlist("first_name")
    last_name = request.POST.getlist("last_name")
    melli_num =request.POST.getlist("melli_number")

    if tour.entire_capacity >= int(number):
            if tour.capacity >= int(number):
                tour.capacity = tour.capacity - int(number)
                tour.entire_capacity= tour.entire_capacity-int(number)
                tour.save()

                number=int(number)
                for i in range(number):

                    userm=request.user.userm
                    gardeshgar=TouristProfile.objects.get(user =userm)
                    wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                                           first_name = first_name[i],last_name= last_name[i],
                                                           meli_code = melli_num[i],
                                                           peygiry_code = 'tour'+'-'+str(tour.id)+'-'+request.user.username)
                    wantedtour = Wanted_Tour.objects.create(gardesh = tour,info=wantedtrip);
    else:
             wrong=True
             form=numberForm(request.POST)
             peopleform=peopleForm(request.POST)

             return render(request, "information_of_buyer_tour.html" , {
                         'username':request.user.username,
                         'tour':tour,
                         'gardesh':gardesh,
                         'form':form,
                         'peopleform':peopleform,
                         'wrong': wrong,
             })

    return render(request, "payment_bank.html",{
        'total_cost': total_cost,
        'tour':tour,
    })


def confirmTour(request,tour_id=''):


        tour=Tour.objects.get(id = tour_id)
        user= request.user.userm
        sender= TouristProfile.objects.get(user = user)
        date = datetime.today()
        amount=request.POST.get("total_cost")
        gardesh=tour.gardesh
        number=int(amount)/tour.cost
        tour.capacity=tour.capacity-number
        tour.entire_capacity=tour.entire_capacity-number
        tour.save()
        info= Trans_info.objects.create(date=date,amount=int(amount),gardesh=gardesh)
        transaction = Trans_Kind1.objects.create(info=info,sender=sender)

        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'kind':'1',
        })



def paymentAirplane(request, airplane_id=''):

    number=request.POST.get("number")
    airplane= AirPlane.objects.get(id = airplane_id)
    cost=airplane.cost
    total_cost=cost * int(number)
    gardesh = airplane.gardesh
    first_name = request.POST.getlist("first_name")
    last_name = request.POST.getlist("last_name")
    melli_num =request.POST.getlist("melli_number")

    if airplane.capacity >= int(number):

                number=int(number)
                userm=request.user.userm
                gardeshgar=TouristProfile.objects.get(user =userm)
                seats=AirplaneSeat.objects.filter(airplane =airplane).filter(full=False)[number]
                for i in range(number):
                    wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                                           first_name = first_name[i],last_name= last_name[i],
                                                           meli_code = melli_num[i],
                                                           peygiry_code = 'airplane'+'-'+str(airplane.id)+'-'+request.user.username)
                  #  seats[i].full=True
                   # seats[i].save()
                    wantedairplane = Wanted_Airplane.objects.create(gardesh = seats[i] ,info=wantedtrip);
                #airplane.capacity=airplane.capacity-number
    else:
             wrong=True
             form=numberForm(request.POST)
             peopleform=peopleForm(request.POST)

             return render(request, "information_of_buyer_service.html" , {
                         'username':request.user.username,
                         'airplane':airplane,
                         'kind':'airplane',
                         'gardesh':gardesh,
                         'form':form,
                         'peopleform':peopleform,
                         'wrong': wrong,
             })

    return render(request, "payment_bank.html",{
        'total_cost': total_cost,
        'airplane':airplane,
    })


def confirmAirplane(request,airplane_id=''):


        airplane=AirPlane.objects.get(id = airplane_id)
        user= request.user.userm
        sender= TouristProfile.objects.get(user = user)
        date = datetime.today()
        amount=request.POST.get("total_cost")
        gardesh=airplane.gardesh
        number=int(amount)/airplane.cost
        airplane.capacity=airplane.capacity-number
        airplane.save()
        seats=AirplaneSeat.objects.filter(airplane =airplane).filter(full=False)[number]
        for i in range(number):
            seats[i].full=True
        info= Trans_info.objects.create(date=date,amount=int(amount),gardesh=gardesh)
        transaction = Trans_Kind1.objects.create(info=info,sender=sender)

        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'kind':'2',
        })


##############################TRAIN######################################################################################


def paymentTrain(request, train_id=''):

    number=request.POST.get("number")
    train= Train.objects.get(id = train_id)
    cost=train.cost
    total_cost=cost * int(number)
    gardesh = train.gardesh
    first_name = request.POST.getlist("first_name")
    last_name = request.POST.getlist("last_name")
    melli_num =request.POST.getlist("melli_number")

    if train.capacity >= int(number):

                number=int(number)
                userm=request.user.userm
                gardeshgar=TouristProfile.objects.get(user =userm)
                seats=TrainSeat.objects.filter(train =train).filter(full=False)[number]
                for i in range(number):
                    wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                                           first_name = first_name[i],last_name= last_name[i],
                                                           meli_code = melli_num[i],
                                                           peygiry_code = 'train'+'-'+str(train.id)+'-'+request.user.username)
                   # seats[i].full=True
                    #seats[i].save()
                    wantedtrain = Wanted_Train.objects.create(gardesh = seats[i] ,info=wantedtrip);
                #train.capacity=train.capacity-number
    else:
             wrong=True
             form=numberForm(request.POST)
             peopleform=peopleForm(request.POST)

             return render(request, "information_of_buyer_service.html" , {
                         'username':request.user.username,
                         'train':train,
                         'kind':'train',
                         'gardesh':gardesh,
                         'form':form,
                         'peopleform':peopleform,
                         'wrong': wrong,
             })

    return render(request, "payment_bank.html",{
        'total_cost': total_cost,
        'train':train,
    })


def confirmTrain(request,train_id=''):


        train=Train.objects.get(id = train_id)
        user= request.user.userm
        sender= TouristProfile.objects.get(user = user)
        date = datetime.today()
        amount=request.POST.get("total_cost")
        gardesh=train.gardesh
        number=int(amount)/train.cost
        train.capacity=train.capacity-number
        train.save()
        seats=AirplaneSeat.objects.filter(airplane =airplane).filter(full=False)[number]
        for i in range(number):
            seats[i].full=True

        info= Trans_info.objects.create(date=date,amount=int(amount),gardesh=gardesh)
        transaction = Trans_Kind1.objects.create(info=info,sender=sender)

        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'kind':'3',
        })

##################################RESTAURANT########################################################################
def paymentRestaurant():
    return

def confirmRestaurant():

    return


##################################HOTEL###############################################################################

def paymentHotel():
    return
    
def confirmHotel():
    return

def ozviyat(request ,username='', password=''):

    return render(request, "payment_ozviyat.html",{
        'total_cost':'۳۰۰۰',
    })

