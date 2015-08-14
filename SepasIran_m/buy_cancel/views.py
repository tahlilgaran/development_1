from django.shortcuts import render
from define_trip.models import *
from buy_cancel.models import *
from .forms import numberForm,peopleForm,hotelForm,tableForm
# Create your views here.

def purchaseResturant(request ,id=''):
    username=request.user.username
    table=Table.objects.get(id = id)
   # table=Table.objects.filter(restaurant = resturant).get(capacity = capacity)
    restaurant=table.restaurant
    gardesh=restaurant.gardesh
    tableform=tableForm(request.POST)
    peopleform=peopleForm(request.POST)
    return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind': 'resturant',
             'resturant': restaurant,
             'table': table,
             'gardesh': gardesh,
             'tableform':tableform,
             'peopleform': peopleform,

            })


def purchaseTour(request ,id=''):

    username=request.user.username
    tour=Tour.objects.get(id = id);
    gardesh=tour.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request, "information_of_buyer_tour.html" , {
             'username':username,
             'tour':tour,
             'gardesh':gardesh,
             'form':form,
             'peopleform':peopleform,
    })


def purchaseAirplane(request ,id=''):
         username=request.user.username
         airplane=AirPlane.objects.get(id = id);
        # airplaneseat=AirplaneSeat.objects.filter(airplane = airplane).filter(full = False)[0]
         gardesh=airplane.gardesh
         form=numberForm(request.POST)
         peopleform=peopleForm(request.POST)
         return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind':'airplane',
             'airplane':airplane,
             'form':form,
             'peopleform':peopleform,
             'gardesh': gardesh,
            })

def purchaseTrain(request ,id=''):
    username=request.user.username
    train=Train.objects.get(id = id);
    gardesh = train.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request, "information_of_buyer_service.html" , {
            'username':username,
             'kind':'train',
             'train':train,
             'form':form,
             'gardesh': gardesh,
             'peopleform':peopleform,

            })

def purchaseHotel(request ,id=''):
    username=request.user.username
    room=Room.objects.get(id = id);
    hotel=room.hotel
    gardesh=hotel.gardesh
    form=numberForm(request.POST)
    hotelform=hotelForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request , "information_of_buyer_service.html" , {
           'username': username,
           'kind': 'hotel',
           'room': room,
           'hotel': hotel,
           'gardesh': gardesh,
           'form':form,
           'hotelform':hotelform,
           'peopleform':peopleform,


        })


def reserveResturant(request ,id=''):
    username=request.user.username
    table=Table.objects.get(id = id)
   # table=Table.objects.filter(restaurant = resturant).get(capacity = capacity)
    restaurant=table.restaurant
    gardesh=restaurant.gardesh
    tableform=tableForm(request.POST)
    peopleform=peopleForm(request.POST)
    return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind': 'resturant',
             'resturant': restaurant,
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
             'form':form,
             'peopleform':peopleform,
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


    username = request.user.username
    number = request.POST.get("number")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    melli_num =request.POST.get("melli_number")

    if kind == 'tour':

        tour = Tour.objects.get(id = id)
        gardesh = tour.gardesh
        if tour.entire_capacity >= int(number):
            if tour.capacity >= int(number):
                tour.capacity = tour.capacity - int(number)
                tour.entire_capacity= tour.entire_capacity-int(number)
                tour.save()

                number=int(number)
                for i in range(number):

                    userm=request.user.userm
                    gardeshgar=TouristProfile.objects.get(user =userm)
                    wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                                           first_name = first_name,last_name= last_name,
                                                           meli_code = melli_num,
                                                           peygiry_code = 'tour'+'-'+str(tour.id)+'-'+request.user.username)
                    wantedtour = Wanted_Tour.objects.create(gardesh = tour,info=wantedtrip);
        else:
             wrong=True
             form=numberForm(request.POST)
             peopleform=peopleForm(request.POST)

             return render(request, "information_of_reserver_tour.html" , {
                         'username':username,
                         'tour':tour,
                         'gardesh':gardesh,
                         'form':form,
                         'peopleform':peopleform,
                         'wrong': wrong,
             })

        return render(request , "reserve_status.html",{
                    'username':username,
                    'number': number,
                    'kind': kind,
                    'gardesh': gardesh,
                    'tour': tour,
        })


    if kind == 'hotel':

            hotel = Hotel.objects.get(id = id)
            gardesh = hotel.gardesh
            if hotel.entire_capacity >= int(number):
                if hotel.capacity >= int(number):
                    hotel.capacity = hotel.capacity - int(number)
                    hotel.entire_capacity= hotel.entire_capacity-int(number)
                    hotel.save()


                    for i in range(number):

                        userm=request.user.userm
                        gardeshgar=TouristProfile.objects.get(user =userm)
                        wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                                               first_name = first_name,last_name= last_name,
                                                               meli_code = melli_num,
                                                               peygiry_code = 'tour'+'-'+str(tour.id)+'-'+request.user.username)
                        wantedtour = Wanted_Tour.objects.create(gardesh = hotel,info=wantedtrip);

            else:
             wrong=True
             form=numberForm(request.POST)
             peopleform=peopleForm(request.POST)

             return render(request, "information_of_reserver_service.html" , {
                         'username':username,
                         'kind': kind,
                         'hotel':hotel,
                         'gardesh':gardesh,
                         'form':form,
                         'peopleform':peopleform,
                         'wrong': wrong,
            })
            return render( request , "reserve_status.html",{
                        'username':username,
                        'number': number,
                        'kind': kind,
                        'gardesh': gardesh,
                        'hotel': hotel,
            })

    if kind == 'restaurant':

            restaurant = Restaurant.objects.get(id = id)
            gardesh = restaurant.gardesh
            if restaurant.entire_capacity >= int(number):
                if restaurant.capacity >= int(number):
                    restaurant.capacity = restaurant.capacity - int(number)
                    restaurant.entire_capacity= restaurant.entire_capacity-int(number)
                    restaurant.save()

                    number=int(number)
                    for i in range(number):

                        userm=request.user.userm
                        gardeshgar=TouristProfile.objects.get(user =userm)
                        wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                                               first_name = first_name,last_name= last_name,
                                                               meli_code = melli_num,
                                                               peygiry_code = 'restaurant'+'-'+str(restaurant.id)+'-'+request.user.username)
                        wantedrestaurant = Wanted_restaurant.objects.create(gardesh = restaurant,info=wantedtrip);
               # else render
            else:
                 wrong=True
                 form=numberForm(request.POST)
                 peopleform=peopleForm(request.POST)

                 return render(request, "information_of_reserver_service.html" , {
                             'username':username,
                             'restaurant':restaurant,
                             'kind':kind,
                             'gardesh':gardesh,
                             'form':form,
                             'peopleform':peopleform,
                             'wrong': wrong,
            })
            return render( request , "reserve_status.html",{
                        'username':username,
                        'number': number,
                        'kind': kind,
                        'gardesh': gardesh,
                        'tour': tour,
            })


    if kind == 'airplane':

            airplane = AirPlane.objects.get(id = id)
            gardesh = airplane.gardesh
            if airplane.entire_capacity >= int(number):
                if airplane.capacity >= int(number):
                    airplane.capacity = airplane.capacity - int(number)
                    airplane.entire_capacity= airplane.entire_capacity-int(number)
                    airplane.save()
                    number=int(number)
                    seats= AirplaneSeat.objects.filter(AirPlane = airplane).filter(full = False)[number]

                    for i in range(number):
                        seats[i].full=True

                    for i in range(number):

                        userm=request.user.userm
                        gardeshgar=TouristProfile.objects.get(user =userm)
                        wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                                               first_name = first_name,last_name= last_name,
                                                               meli_code = melli_num,
                                                               peygiry_code = 'airplane'+'-'+str(airplane.id)+'-'+request.user.username)
                        wantedairplane = Wanted_airplane.objects.create(gardesh = airplane,info=wantedtrip);
               # else render
            else:

                 wrong=True
                 form=numberForm(request.POST)
                 peopleform=peopleForm(request.POST)

                 return render(request, "information_of_reserver_service.html" , {
                             'username':username,
                             'airplane':airplane,
                             'kind':kind,
                             'gardesh':gardesh,
                             'form':form,
                             'peopleform':peopleform,
                             'wrong': wrong,
            })
            return render( request , "reserve_status.html",{
                        'username':username,
                        'number': number,
                        'kind': kind,
                        'gardesh': gardesh,
                        'airplane': airplane,
            })

    if kind == 'train':

            train = Train.objects.get(id = id)
            gardesh = train.gardesh
            if train.entire_capacity >= int(number):
                if train.capacity >= int(number):
                    train.capacity = train.capacity - int(number)
                    train.entire_capacity= train.entire_capacity-int(number)
                    train.save()

                    number=int(number)
                    for i in range(number):

                        userm=request.user.userm
                        gardeshgar=TouristProfile.objects.get(user =userm)
                        wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                                               first_name = first_name,last_name= last_name,
                                                               meli_code = melli_num,
                                                               peygiry_code = 'train'+'-'+str(train.id)+'-'+request.user.username)
                        wantedtrain = Wanted_train.objects.create(gardesh = train,info=wantedtrip);
               # else render
            else:

                 wrong=True
                 form=numberForm(request.POST)
                 peopleform=peopleForm(request.POST)

                 return render(request, "information_of_reserver_service.html" , {
                             'username':username,
                             'train':train,
                             'kind':kind,
                             'gardesh':gardesh,
                             'form':form,
                             'peopleform':peopleform,
                             'wrong': wrong,
            })
            return render( request , "reserve_status.html",{
                        'username':username,
                        'number': number,
                        'kind': kind,
                        'gardesh': gardesh,
                        'train': train,
            })

