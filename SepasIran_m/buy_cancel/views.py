from django.shortcuts import render
from define_trip.models import *

# Create your views here.
def purchase(request ,kind='',username='',id=''):

  # these 2 line for test
    id = 1
    username = "unique"
    kind = 'resturant'# notice!


    if kind=='tour':
         tour=Tour.objects.get(id = id);
         return render(request, "information_of_buyer_tour.html" , {
             'username':username,
             'tour':tour,
         })
    else:
        if kind=='airplane':
            airplane=Airplane.objects.get(id = id);
            #airplane=airplaneseat.airplane
            gardesh=airplane.gardesh
            return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind':kind,
             'airplane':airplane,
             #'airplaneseat': airplaneseat,
             'gardesh': gardesh,
            })
        elif kind=='train':
            train=Train.objects.get(id = id);
           # train=trainseat.train
            gardesh = train.gardesh
            return render(request, "information_of_buyer_service.html" , {
            'username':username,
             'kind':kind,
             'train':train,
            # 'trainsear': trainseat,
             'gardesh': gardesh,

            })
        elif kind == 'resturant':
            table = Table.objects.get(id = id);
            resturant =table.restaurant
            gardesh=resturant.gardesh

            return render(request, "information_of_buyer_service.html" , {
             'username': username,
             'kind': kind,
             'resturant': resturant,
             'table': table,
             'gardesh': gardesh,

            })

        room=Room.objects.get(id = id);
        hotel=room.hotel
        gardesh=hotel.gardesh

        return render(request , "information_of_buyer_service.html" , {
           'username': username,
           'kind': kind,
           'room': room,
           'hotel': hotel,
           'gardesh': gardesh,


        })

          #return render(request, "reservation-status.html")



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

    # these 2 line for test
    id = 1
    username = "unique"
    kind = 'resturant'# notice!


    if kind=='tour':
         tour=Tour.objects.get(id = id);
         return render(request, "information_of_reserver_tour.html" , {
             'username':username,
             'tour':tour,
         })
    else:
        if kind=='airplane':
            airplaneseat=AirplaneSeat.objects.get(id = id);
            airplane=airplaneseat.airplane
            gardesh=airplane.gardesh
            return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind':kind,
             'airplane':airplane,
             'airplaneseat': airplaneseat,
             'gardesh': gardesh,
            })
        elif kind=='train':
            trainseat=TrainSeat.objects.get(id = id);
            train=trainseat.train
            gardesh = train.gardesh
            return render(request, "information_of_reserver_service.html" , {
            'username':username,
             'kind':kind,
             'train':train,
             'trainsear': trainseat,
             'gardesh': gardesh,

            })
        elif kind == 'resturant':
            table = Table.objects.get(id = id);
            resturant =table.restaurant
            gardesh=resturant.gardesh

            return render(request, "information_of_reserver_service.html" , {
             'username': username,
             'kind': kind,
             'resturant': resturant,
             'table': table,
             'gardesh': gardesh,

            })

        room=Room.objects.get(id = id);
        hotel=room.hotel
        gardesh=hotel.gardesh

        return render(request , "information_of_reserver_service.html" , {
           'username': username,
           'kind': kind,
           'room': room,
           'hotel': hotel,
           'gardesh': gardesh,


        })

  # return render(request, "reservation-status.html" )

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

