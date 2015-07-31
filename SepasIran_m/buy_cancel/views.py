from django.shortcuts import render
from define_trip.models import *

# Create your views here.

def purchaseResturant(request ,capacity='',id='',username=''):
    resturant=Restaurant.objects.get(id = id)
    table=Table.objects.filter(resturant = resturant).get(capacity = capacity)[0]
    gardesh=resturant.gardesh

    return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind': 'resturant',
             'resturant': resturant,
             'table': table,
             'gardesh': gardesh,

            })


def purchaseTour(request ,id='',username=''):
    tour=Tour.objects.get(id = id);
    return render(request, "information_of_buyer_tour.html" , {
             'username':username,
             'tour':tour,
    })


def purchaseAirplane(request ,id='', username=''):
         airplane=AirPlane.objects.get(id = id);
         airplaneseat=AirplaneSeat.objects.filter(airplane = airplane).filter(full = False)[0]
         gardesh=airplane.gardesh
         return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind':'airplane',
             'airplane':airplane,
             'airplaneseat': airplaneseat,
             'gardesh': gardesh,
            })

def purchaseTrain(request ,id='', username=''):
    train=Train.objects.get(id = id);
    trainseat=TrainSeat.objects.filter(train = train).filter(full = False)[0]
    gardesh = train.gardesh
    return render(request, "information_of_buyer_service.html" , {
            'username':username,
             'kind':'train',
             'train':train,
             'trainsear': trainseat,
             'gardesh': gardesh,

            })

def purchaseHotel(request ,id='', username=''):
    room=Room.objects.get(id = id);
    hotel=room.hotel
    gardesh=hotel.gardesh
    return render(request , "information_of_buyer_service.html" , {
           'username': username,
           'kind': 'hotel',
           'room': room,
           'hotel': hotel,
           'gardesh': gardesh,


        })


def reserveResturant(request ,capacity='',id='',username=''):
    resturant=Restaurant.objects.get(id = id)
    table=Table.objects.filter(resturant = resturant).get(capacity = capacity)[0]
    gardesh=resturant.gardesh

    return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind': 'resturant',
             'resturant': resturant,
             'table': table,
             'gardesh': gardesh,

            })


def reserveTour(request ,id='',username=''):
    tour=Tour.objects.get(id = id);
    return render(request, "information_of_reserver_tour.html" , {
             'username':username,
             'tour':tour,
    })


def reserveAirplane(request ,id='', username=''):
         airplane=AirPlane.objects.get(id = id);
         airplaneseat=AirplaneSeat.objects.filter(airplane = airplane).filter(full = False)[0]
         gardesh=airplane.gardesh
         return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind':'airplane',
             'airplane':airplane,
             'airplaneseat': airplaneseat,
             'gardesh': gardesh,
            })

def reserveTrain(request ,id='', username=''):
    train=Train.objects.get(id = id);
    trainseat=TrainSeat.objects.filter(train = train).filter(full = False)[0]
    gardesh = train.gardesh
    return render(request, "information_of_reserver_service.html" , {
            'username':username,
             'kind':'train',
             'train':train,
             'trainsear': trainseat,
             'gardesh': gardesh,

            })

def reserveHotel(request ,id='', username=''):
    room=Room.objects.get(id = id);
    hotel=room.hotel
    gardesh=hotel.gardesh
    return render(request , "information_of_reserver_service.html" , {
           'username': username,
           'kind': 'hotel',
           'room': room,
           'hotel': hotel,
           'gardesh': gardesh,


        })


def confirmReserve(request,id=''):
    start_time = request.POST.get("start_time","")
    end_time = request.POST.get("end_time","")
    date = request.POST.get("date","")


    # TableReserve.filter(table=table,date=date,end_time=end_time,start_time=start_time)
    # check
    # res = False

    # if ! res:
    #     msg = "this table is already reserved"
    #     return render(request,
    #                   {'msg':msg,
    #                    }
    #                   )
    #
    #



    return;

