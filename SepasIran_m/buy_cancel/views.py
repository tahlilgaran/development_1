from django.shortcuts import render
from define_trip.models import *
from buy_cancel.models import *
from accounting.models import *
from .forms import numberForm,peopleForm,bankForm
from django.http import HttpResponseRedirect

# Create your views here.

def purchaseRestaurant(request ,id=''):
    username=request.user.username
    user2=request.user
    restaurant=Restaurant.objects.get(id = id)
    ID=request.POST.get("returned_id_list")

    tableID = ID.split(',')
    print(tableID)
    table_list=[]
    i=0
    total=0
    for table in tableID:

        table_list.append(Table.objects.get(id=table))
        total += table_list[i].cost_perClock
        i += 1
    gardesh=restaurant.gardesh
    peopleform=peopleForm(request.POST)
    return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind': 'restaurant',
             'restaurant': restaurant,
             'tableList': table_list,
             'ID':ID,
             'gardesh': gardesh,
             'peopleform': peopleform,
             'total_cost':total,
             'user2':user2,

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
    user2=request.user
    hotel=Hotel.objects.get(id = id)
    ID=request.POST.get("returned_id_list")

    roomID = ID.split(',')

    room_list=[]
    i=0
    total=0
    for table in roomID:

        room_list.append(Table.objects.get(id=table))
        total += room_list[i].cost_perClock
        i += 1
    gardesh=hotel.gardesh
    peopleform=peopleForm(request.POST)
    return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind': 'hotel',
             'hotel': hotel,
             'roomList': room_list,
             'gardesh': gardesh,
             'ID':ID,
             'peopleform': peopleform,
             'total_cost':total,
             'user2':user2,

     })

def reserveResturant(request ,id=''):
    username=request.user.username
    user2=request.user
    restaurant=Restaurant.objects.get(id = id)
    ID=request.POST.get("returned_id_list")

    tableID = ID.split(',')
    print(tableID)
    table_list=[]
    i=0
    total=0
    for table in tableID:

        table_list.append(Table.objects.get(id=table))
        total += table_list[i].cost_perClock
        i += 1
    gardesh=restaurant.gardesh
    peopleform=peopleForm(request.POST)
    return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind': 'restaurant',
             'restaurant': restaurant,
             'tableList': table_list,
             'ID':ID,
             'gardesh': gardesh,
             'peopleform': peopleform,
             'total_cost':total,
             'user2':user2,

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
             'gardesh':gardesh,
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
    user2=request.user
    hotel=Hotel.objects.get(id = id)
    ID=request.POST.get("returned_id_list")

    roomID = ID.split(',')

    room_list=[]
    i=0
    total=0
    for table in roomID:

        room_list.append(Table.objects.get(id=table))
        total += room_list[i].cost_perClock
        i += 1
    gardesh=hotel.gardesh
    peopleform=peopleForm(request.POST)
    return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind': 'hotel',
             'hotel': hotel,
             'roomList': room_list,
             'ID':ID,
             'gardesh': gardesh,
             'peopleform': peopleform,
             'total_cost':total,
             'user2':user2,

     })


def statusReserve(request,kind='', id=''):


    username = request.user.username
    number = request.POST.get("number")
    first_name = request.POST.getlist("first_name")
    last_name = request.POST.getlist("last_name")
    melli_num =request.POST.getlist("melli_number")
    wrong = False
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
                                                           first_name = first_name[i],last_name= last_name[i],
                                                           meli_code = melli_num[i],
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
                                                               peygiry_code = 'tour'+'-'+str(hotel.id)+'-'+request.user.username)
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
                        wantedrestaurant = Wanted_Restaurant.objects.create(gardesh = restaurant,info=wantedtrip);
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
                        'restaurant': restaurant,
            })


    if kind == 'airplane':

            airplane = AirPlane.objects.get(id = id)
            gardesh = airplane.gardesh

            if airplane.capacity >= int(number):
                    airplane.capacity = airplane.capacity - int(number)
                    airplane.save()
                    number=int(number)
                    seats= AirplaneSeat.objects.filter(airplane = airplane,full = False)
                    i=0
                    for seat in seats:
                        if i == number:
                            break
                        else:
                            seat.full=True
                            seat.save()

                            userm=request.user.userm
                            gardeshgar=TouristProfile.objects.get(user =userm)
                            wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                                                   first_name = first_name[i],last_name= last_name[i],
                                                                   meli_code = melli_num[i],
                                                                   peygiry_code = 'airplane'+'-'+str(seat.id)+'-'+request.user.username)
                            wantedairplane = Wanted_Airplane.objects.create(gardesh = seat,info=wantedtrip);
                            i += 1
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

            if train.capacity >= int(number):
                    train.capacity = train.capacity - int(number)
                    train.save()

                    number=int(number)
                    seats= TrainSeat.objects.filter(train = train,full = False)
                    i=0

                    for seat in seats:
                        if i == number:
                            break
                        else:
                            seat.full=True
                            seat.save()



                            userm=request.user.userm
                            gardeshgar=TouristProfile.objects.get(user =userm)
                            wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                                                   first_name = first_name[i],last_name= last_name[i],
                                                                   meli_code = melli_num[i],
                                                                   peygiry_code = 'train'+'-'+str(seat.id)+'-'+request.user.username)
                            wantedtrain = Wanted_Train.objects.create(gardesh = seat,info=wantedtrip);
                            i += 1
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

####################################################################################################################

def cancel(request , id=''):

    wanted_trip = Wanted_Trip.objects.get(id = id)
    status= wanted_trip.status
    gardeshgar= wanted_trip.gardeshgar
    first_name=wanted_trip.first_name
    last_name= wanted_trip.last_name
    melli_num= wanted_trip.meli_code
    code= str(wanted_trip.peygiry_code)
    codes=code.split("-")
    bankform=bankForm(request.POST)
    wanted_trip.delete()
    if status == 'reserve':
        if codes[0] == 'tour':
            id=int(codes[1])
            tour=Tour.objects.get(id= id)
            tour.capacity += 1
            tour.save()
            wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='cancel',
                                                   first_name = first_name,last_name= last_name,
                                                   meli_code = melli_num,
                                                   peygiry_code = 'tour'+'-'+str(tour.id)+'-'+request.user.username)
            wantedtour = Wanted_Tour.objects.create(gardesh = tour,info=wantedtrip);
            return  HttpResponseRedirect('/userpage/')
        elif codes[0] == 'airplane':
            id=int(codes[1])
            seat=AirplaneSeat.objects.get(id= id)
            seat.full=False
            seat.save()
            airplane=seat.airplane
            airplane.capacity +=1
            wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='cancel',
                                                   first_name = first_name,last_name= last_name,
                                                   meli_code = melli_num,
                                                   peygiry_code = 'airplane'+'-'+str(seat.id)+'-'+request.user.username)
            wantedtour = Wanted_Airplane.objects.create(gardesh = seat,info=wantedtrip);
            return  HttpResponseRedirect('/userpage/')
        elif codes[0] == 'train':
            id=int(codes[1])
            seat=TrainSeat.objects.get(id= id)
            seat.full=False
            seat.save()
            train=seat.train
            train.capacity +=1
            wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='cancel',
                                                   first_name = first_name,last_name= last_name,
                                                   meli_code = melli_num,
                                                   peygiry_code = 'train'+'-'+str(seat.id)+'-'+request.user.username)
            wantedtour = Wanted_Train.objects.create(gardesh = seat,info=wantedtrip);
            return  HttpResponseRedirect('/userpage/')
        elif codes[0] == 'restaurant':

            return

    else:
        if codes[0] == 'tour':
            id=int(codes[1])
            tour=Tour.objects.get(id= id)
            tour.capacity += 1
            tour.save()

            wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='cancel',
                                                   first_name = first_name,last_name= last_name,
                                                   meli_code = melli_num,
                                                   peygiry_code = 'tour'+'-'+str(tour.id)+'-'+request.user.username)
            wantedtour = Wanted_Tour.objects.create(gardesh = tour,info=wantedtrip);

            cost=tour.cost
            free=float(tour.gardesh.free)
            percent=int(float(free)*100)
            account=int(cost-cost*free)
            gardesh=tour.gardesh
            gardeshID = int(gardesh.id)
            gardeshgarID = int(gardeshgar.id)
            print(gardeshID)
            return  render(request, "tasviye_gardeshgar.html",{
                'account':account,
                'gardesh':gardesh,
                'gardeshID': gardeshID,
                'percent':percent,
                'gardeshgarID':gardeshgarID,
                'bankform':bankform,
            })
        elif codes[0] == 'airplane':
            id=int(codes[1])
            seat=AirplaneSeat.objects.get(id= id)
            airplane=seat.airplane
            seat.full=False
            seat.save()
            airplane.capacity += 1
            wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='cancel',
                                                   first_name = first_name,last_name= last_name,
                                                   meli_code = melli_num,
                                                   peygiry_code = 'airplane'+'-'+str(seat.id)+'-'+request.user.username)
            wantedtour = Wanted_Airplane.objects.create(gardesh = seat,info=wantedtrip);

            cost=airplane.cost
            free=float(airplane.gardesh.free)
            percent=int(float(free)*100)
            account=int(cost-cost*free)
            gardesh=airplane.gardesh
            gardeshID = int(gardesh.id)
            gardeshgarID = int(gardeshgar.id)
            print(gardeshID)
            return  render(request, "tasviye_gardeshgar.html",{
                'account':account,
                'gardesh':gardesh,
                'gardeshID': gardeshID,
                'percent':percent,
                'gardeshgarID':gardeshgarID,
                'bankform':bankform,
            })

        elif codes[0] == 'train':
            id=int(codes[1])
            seat=TrainSeat.objects.get(id= id)
            train=seat.train
            seat.full=False
            seat.save()
            train.capacity += 1
            wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='cancel',
                                                   first_name = first_name,last_name= last_name,
                                                   meli_code = melli_num,
                                                   peygiry_code = 'train'+'-'+str(seat.id)+'-'+request.user.username)
            wantedtour = Wanted_Train.objects.create(gardesh = seat,info=wantedtrip);
            cost=train.cost

            free=float(train.gardesh.free)
            percent=int(float(free)*100)
            account=int(cost-cost*free)
            gardesh=train.gardesh
            gardeshID = int(gardesh.id)
            gardeshgarID = int(gardeshgar.id)
            print(gardeshID)
            return  render(request, "tasviye_gardeshgar.html",{
                'account':account,
                'gardesh':gardesh,
                'gardeshID': gardeshID,
                'percent':percent,
                'gardeshgarID':gardeshgarID,
                'bankform':bankform,
            })

        elif codes[0] == 'restaurant':
            return
#####################################################################################################################

def purchaseReserved(request, id=''):

    wanted_trip=Wanted_Trip.objects.get(id =id)
    gardeshgar= wanted_trip.gardeshgar
    first_name=wanted_trip.first_name
    last_name= wanted_trip.last_name
    melli_num= wanted_trip.meli_code
    code= str(wanted_trip.peygiry_code)
    codes=code.split("-")

    if codes[0]== 'tour':

         tour= Tour.objects.get(id = int(codes[1]))
         total_cost=tour.cost
         gardesh = tour.gardesh

         wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                                first_name = first_name,last_name= last_name,
                                                meli_code = melli_num,
                                                peygiry_code = 'tour'+'-'+str(tour.id)+'-'+'reserved')
         wantedtour = Wanted_Tour.objects.create(gardesh = tour,info=wantedtrip);

         return render(request, "payment_bank.html",{
            'total_cost': total_cost,
            'tour':tour,
            'kind':'tour',
         })

    elif codes[0]=='airplane':
         seat= AirplaneSeat.objects.get(id = int(codes[1]))
         airplane=seat.airplane
         total_cost=airplane.cost
         gardesh = airplane.gardesh

         wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                                first_name = first_name,last_name= last_name,
                                                meli_code = melli_num,
                                                peygiry_code = 'airplane'+'-'+str(seat.id)+'-'+'reserved')
         wantedtour = Wanted_Airplane.objects.create(gardesh = seat,info=wantedtrip);

         return render(request, "payment_bank.html",{
            'total_cost': total_cost,
            'airplane':airplane,
            'kind':'airplane',
         })
    elif codes[0]=='train':
         seat= TrainSeat.objects.get(id = int(codes[1]))
         train=seat.train
         total_cost=train.cost
         gardesh = train.gardesh

         wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                                first_name = first_name,last_name= last_name,
                                                meli_code = melli_num,
                                                peygiry_code = 'train'+'-'+str(seat.id)+'-'+'reserved')
         wantedtour = Wanted_Train.objects.create(gardesh = seat,info=wantedtrip);

         return render(request, "payment_bank.html",{
            'total_cost': total_cost,
            'train':train,
            'kind':'train',
         })
