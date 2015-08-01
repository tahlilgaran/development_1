from django.shortcuts import render
from define_trip.models import *
from .forms import numberForm,peopleForm,hotelForm,tableForm
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


def reserveResturant(request ,id='', capacity=''):
    username=request.user.username
    resturant=Restaurant.objects.get(id = id)
    table=Table.objects.filter(restaurant = resturant).get(capacity = capacity)

    gardesh=resturant.gardesh
    tableform=tableForm(request.POST)
    peopleform=peopleForm(request.POST)
    return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind': 'resturant',
             'resturant': resturant,
             'table': table,
             'gardesh': gardesh,
             'tableform':tableform,
             'peopleform': peopleform,

            })


def reserveTour(request ,id='',number=''):

    username=request.user.username
    tour=Tour.objects.get(id = id);
    gardesh=tour.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request, "information_of_reserver_tour.html" , {
             'username':username,
             'tour':tour,
             'gardesh':gardesh,
             'form':form,
             'peopleform':peopleform,
    })

    return render(request, "information_of_reserver_tour.html" , {
             'username':username,
             'tour':tour,
             'gardesh':gardesh,
             'form':form,
             'peopleform':peopleform,
             'isclick': True,
    })


def reserveAirplane(request ,id=''):
         username=request.user.username
         airplane=AirPlane.objects.get(id = id);
        # airplaneseat=AirplaneSeat.objects.filter(airplane = airplane).filter(full = False)[0]
         gardesh=airplane.gardesh
         form=numberForm(request.POST)
         peopleform=peopleForm(request.POST)
         return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind':'airplane',
             'airplane':airplane,
              'form':form,
             'peopleform':peopleform,
             'gardesh': gardesh,
            })

def reserveTrain(request ,id=''):
    username=request.user.username
    train=Train.objects.get(id = id);
    gardesh = train.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request, "information_of_reserver_service.html" , {
            'username':username,
             'kind':'train',
             'train':train,
             'form':form,
             'gardesh': gardesh,
             'peopleform':peopleform,

            })

def reserveHotel(request ,id=''):
    username=request.user.username
    room=Room.objects.get(id = id);
    hotel=room.hotel
    gardesh=hotel.gardesh
    form=numberForm(request.POST)
    hotelform=hotelForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request , "information_of_reserver_service.html" , {
           'username': username,
           'kind': 'hotel',
           'room': room,
           'hotel': hotel,
           'gardesh': gardesh,
           'form':form,
           'hotelform':hotelform,
           'peopleform':peopleform,


        })


def statusReserve(request,kind='', id=''):

    #if kind == 'restaurant':
     #todo check zarfiyat va taghir an
  table=Table.objects.get(id = id)
  restaurant= table.restaurant
  gardesh=restaurant.gardesh
  return render("reserve-status.html",{
            'kind':'restaurant',
            'table':table,
            'gardesh':gardesh,
  })


  if kind == 'tour':
        error = False
        number = request.POST.get("number","")
        tour = Tour.objects.get(id = id)
        gardesh = tour.gardesh
        #if tour.capacity < int(number):
         #   msg = "ظرفیت به اندازه ی کافی برای رزرو شما وجود ندارد"
          #  error = True
           # return render ("information_of_reserver_tour.html",{
            #    'error' : error,
             #   'msg': msg,
            #})

       # tour.capacity = int(tour.capacity)- int(number)
        #tour.save()
        return render("reserve-status.html", {
                'number': number,
                'kind': 'tour',
                'gardesh': gardesh,
                'tour': tour,
        })



