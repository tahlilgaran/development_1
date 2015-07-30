from django.shortcuts import render
from define_trip.models import *

# Create your views here.
def purchase(request ,kind='',username='',id=''):

 # these 2 line for test
    id = 1
    username = "unique"
    kind = 'tour'# notice!


    if kind=='tour':
         tour=Tour.objects.get(id = id);
         return render(request, "information_of_buyer_tour.html" , {
             'username':username,
             'tour':tour,
         })
    else:
        if kind=='airplane':
            airplaneseat=AirplaneSeat.objects.get(id = id);
            airplane=airplaneseat.airplane
            return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind':kind,
             'airplane':airplane,
             'airplanesear': airplaneseat,
            })
        elif kind=='train':
            trainseat=TrainSeat.objects.get(id = id);
            train=trainseat.train
            return render(request, "information_of_buyer_service.html" , {
            'username':username,
             'kind':kind,
             'train':train,
             'trainsear': trainseat,
            })
        elif kind == 'resturant':
            table = Table.objects.get(id = id);
            resturant =table.restaurant
            return render(request, "information_of_buyer_service.html" , {
             'username': username,
             'kind': kind,
             'resturant': resturant,
             'table': table,
            })

        room=Room.objects.get(id = id);
        hotel=room.hotel
        return render(request , "information_of_buyer_service.html" , {
           'username': username,
           'kind': kind,
           'room': room,
           'hotel': hotel,

        })

          #return render(request, "reservation-status.html")



def reserve(request ,kind='',username='',id=''):

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
            return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind':kind,
             'airplane':airplane,
             'airplanesear': airplaneseat,
            })
        elif kind=='train':
            trainseat=TrainSeat.objects.get(id = id);
            train=trainseat.train
            return render(request, "information_of_reserver_service.html" , {
            'username':username,
             'kind':kind,
             'train':train,
             'trainsear': trainseat,
            })
        elif kind == 'resturant':
            table = Table.objects.get(id = id);
            resturant =table.restaurant
            return render(request, "information_of_reserver_service.html" , {
             'username': username,
             'kind': kind,
             'resturant': resturant,
             'table': table,
            })

        room=Room.objects.get(id = id);
        hotel=room.hotel
        return render(request , "information_of_reserver_service.html" , {
           'username': username,
           'kind': kind,
           'room': room,
           'hotel': hotel,

        })

  # return render(request, "reservation-status.html" )

def confirmreserve(request,id=''):
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

