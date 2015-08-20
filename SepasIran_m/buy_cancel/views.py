from django.shortcuts import render
from define_trip.models import *
from buy_cancel.models import *
from accounting.models import *
from buy_cancel.forms import numberForm,peopleForm,bankForm
from django.http import HttpResponseRedirect

# Create your views here.
tarikh=datetime.datetime.now()
def purchaseRestaurant(request ,id=''):
    tarikh=datetime.datetime.now()
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
              'position':'زیر سامانه ی خرید',
                'tarikh':tarikh,


     })


def purchaseTour(request ,id=''):

    username=request.user.username
    user2=request.user
    tour=Tour.objects.get(id = id);
    gardesh=tour.gardesh


    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)
    tarikh=datetime.datetime.now()
    return render(request, "information_of_buyer_tour.html" , {
             'username':username,
             'tour':tour,
             'gardesh':gardesh,
             'form':form,
             'peopleform':peopleform,
            'user2':user2,
             'position':'زیر سامانه ی خرید',
            'tarikh':tarikh,

    })


def purchaseAirplane(request ,id=''):
         username=request.user.username
         user2=request.user
         tarikh=datetime.datetime.now()
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
             'user2':user2,
             'position':'زیر سامانه ی خرید',
             'tarikh':tarikh


            })

def purchaseTrain(request ,id=''):
    username=request.user.username
    user2=request.user
    tarikh=datetime.datetime.now()
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
        'user2':user2,
        'position':'زیر سامانه ی خرید',
        'tarikh':tarikh,


            })

def purchaseHotel(request ,id=''):
    username=request.user.username
    user2=request.user
    tarikh=datetime.datetime.now()
    hotel=Hotel.objects.get(id = id)
    ID=request.POST.get("returned_id_list")

    roomID = ID.split(',')

    room_list=[]
    i=0
    total=0
    for table in roomID:

        room_list.append(Room.objects.get(id=table))
        total += room_list[i].cost_perNight
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
        'position':'زیر سامانه ی خرید',
        'tarikh':tarikh,


     })

def reserveRestaurant(request ,id=''):
    username=request.user.username
    user2=request.user
    restaurant=Restaurant.objects.get(id = id)
    ID=request.POST.get("returned_id_list")
    tarikh=datetime.datetime.now()
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
                'position':'زیر سامانه ی رزرو',
        'tarikh':tarikh,


     })


def reserveTour(request ,id='',number=''):

    username=request.user.username
    user2=request.user
    tour=Tour.objects.get(id = id);
    gardesh=tour.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)
    tarikh=datetime.datetime.now()

    return render(request, "information_of_reserver_tour.html" , {
             'username':username,
             'tour':tour,
             'form':form,
             'peopleform':peopleform,
             'gardesh':gardesh,
        'user2':user2,
        'position':'زیر سامانه ی رزرو',
        'tarikh':tarikh,

    })




def reserveAirplane(request ,id=''):
         username=request.user.username
         airplane=AirPlane.objects.get(id = id);
         user2=request.user
         tarikh=datetime.datetime.now()
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
             'user2':user2,
              'position':'زیر سامانه ی رزرو',
             'tarikh':tarikh,

            })

def reserveTrain(request ,id=''):
    username=request.user.username
    train=Train.objects.get(id = id);
    gardesh = train.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)
    user2=request.user
    tarikh=datetime.datetime.now()
    return render(request, "information_of_reserver_service.html" , {
            'username':username,
             'kind':'train',
             'train':train,
             'form':form,
             'gardesh': gardesh,
             'peopleform':peopleform,
        'user2':user2,
         'position':'زیر سامانه ی رزرو',
        'tarikh':tarikh,


            })

def reserveHotel(request ,id=''):
    username=request.user.username
    user2=request.user
    hotel=Hotel.objects.get(id = id)
    ID=request.POST.get("returned_id_list")
    tarikh=datetime.datetime.now()
    roomID = ID.split(',')

    room_list=[]
    i=0
    total=0
    for table in roomID:

        room_list.append(Room.objects.get(id=table))
        total += room_list[i].cost_perNight
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
         'position':'زیر سامانه ی رزرو',
        'tarikh':tarikh,


     })


def statusReserve(request,kind='', id=''):

    tarikh=datetime.datetime.now()
    username = request.user.username
    user2= request.user
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
                 'user2':user2,
                  'position':'زیر سامانه ی رزرو',
                 'tarikh':tarikh,

             })

        return render(request , "reserve_status.html",{
                    'username':username,
                    'number': number,
                    'kind': kind,
                    'gardesh': gardesh,
                    'tour': tour,
            'user2':user2,
             'position':'زیر سامانه ی رزرو',
            'tarikh':tarikh,

        })


    if kind == 'hotel':
          hotel=Hotel.objects.get(id = id)
          user= request.user.userm

          list= request.POST.get("ID")
          roomIDList=list.split(',')

          for t in roomIDList:
                room=Room.objects.get(id = t)
                room.full=True
                room.save()

                gardeshgar=TouristProfile.objects.get(user =user)
                wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                                       first_name = first_name,last_name= last_name,
                                                       meli_code = melli_num,
                                                       peygiry_code = 'hotel'+'-'+str(hotel.id)+'-'+request.user.username)
                wantedtour = Wanted_Hotel.objects.create(gardesh = room,info=wantedtrip);


          return render( request , "reserve_status.html",{
                        'username':username,
                        'number': number,
                        'kind': kind,
                        'gardesh': hotel.gardesh,
                        'hotel': hotel,
              'user2':user2,
               'position':'زیر سامانه ی رزرو',
              'tarikh':tarikh,

          })


    if kind == 'restaurant':

          restaurant=Restaurant.objects.get(id = id)
          user= request.user.userm

          list= request.POST.get("ID")
          tableIDList=list.split(',')

          for t in tableIDList:
                table=Table.objects.get(id = t)
                table.full=True
                table.save()

                gardeshgar=TouristProfile.objects.get(user =user)
                wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                                       first_name = first_name,last_name= last_name,
                                                       meli_code = melli_num,
                                                       peygiry_code = 'restaurant'+'-'+str(table.id)+'-'+request.user.username)
                wantedtour = Wanted_Restaurant.objects.create(gardesh = table,info=wantedtrip);


          return render( request , "reserve_status.html",{
                        'username':username,
                        'number': number,
                        'kind': kind,
                        'gardesh': restaurant.gardesh,
                        'restaurant': restaurant,
              'tarikh':tarikh,
              'user2':user2,
               'position':'زیر سامانه ی رزرو',

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
                     'tarikh':tarikh,
                     'user2':user2,
                      'position':'زیر سامانه ی رزرو',

            })
            return render( request , "reserve_status.html",{
                        'username':username,
                        'number': number,
                        'kind': kind,
                        'gardesh': gardesh,
                        'airplane': airplane,
                'user2':user2,
                 'position':'زیر سامانه ی رزرو',
                'tarikh':tarikh,

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
                     'tarikh':tarikh,
                     'user2':user2,
                      'position':'زیر سامانه ی رزرو',

            })
            return render( request , "reserve_status.html",{
                        'username':username,
                        'number': number,
                        'kind': kind,
                        'gardesh': gardesh,
                        'train': train,
                'user2':user2,
                'tarikh':tarikh,
                 'position':'زیر سامانه ی رزرو',


            })

####################################################################################################################

def cancel(request , id=''):

    wanted_trip = Wanted_Trip.objects.get(id = id)
    user2=request.user
    status= wanted_trip.status
    gardeshgar= wanted_trip.gardeshgar
    first_name=wanted_trip.first_name
    last_name= wanted_trip.last_name
    melli_num= wanted_trip.meli_code
    code= str(wanted_trip.peygiry_code)
    codes=code.split("-")
    bankform=bankForm(request.POST)

    if status == 'reserve':
        if codes[0] == 'tour':
            id=int(codes[1])
            tour=Tour.objects.get(id= id)
            tour.capacity += 1
            tour.save()
            Wanted_Tour.objects.get(info=wanted_trip).delete()
            wanted_trip.delete()

            return  HttpResponseRedirect('/userpage/',{
                'user2':user2,
            })
        elif codes[0] == 'airplane':
            id=int(codes[1])
            seat=AirplaneSeat.objects.get(id= id)
            seat.full=False
            seat.save()
            airplane=seat.airplane
            airplane.capacity +=1
            Wanted_Airplane.objects.get(info=wanted_trip).delete()
            wanted_trip.delete()

            return  HttpResponseRedirect('/userpage/')
        elif codes[0] == 'train':
            id=int(codes[1])
            seat=TrainSeat.objects.get(id= id)
            seat.full=False
            seat.save()
            train=seat.train
            train.capacity +=1
            Wanted_Train.objects.get(info=wanted_trip).delete()
            wanted_trip.delete()

            return  HttpResponseRedirect('/userpage/')
        elif codes[0] == 'restaurant':
            id=int(codes[1])
            seat=Table.objects.get(id= id)
            seat.full=False
            seat.save()
            Wanted_Restaurant.objects.get(info=wanted_trip).delete()
            wanted_trip.delete()

            return  HttpResponseRedirect('/userpage/')

        elif codes[0] == 'hotel':
            id=int(codes[1])
            seat=Room.objects.get(id= id)
            seat.full=False
            seat.save()
            Wanted_Hotel.objects.get(info=wanted_trip).delete()
            wanted_trip.delete()

            return  HttpResponseRedirect('/userpage/')



    else:
        if codes[0] == 'tour':
            id=int(codes[1])
            tour=Tour.objects.get(id= id)
            tour.capacity += 1
            tour.save()
            Wanted_Tour.objects.get(info=wanted_trip).delete()
            wanted_trip.delete()

            cost=tour.cost

            account=int(cost-cost*0.05)
            gardesh=tour.gardesh
            gardeshID = int(gardesh.id)
            gardeshgarID = int(gardeshgar.id)
            print(gardeshID)
            return  render(request, "tasviye_gardeshgar.html",{
                'account':account,
                'gardesh':gardesh,
                'gardeshID': gardeshID,
                'gardeshgarID':gardeshgarID,
                'bankform':bankform,
                 'position':'زیر سامانه ی حسابداری',
                'tarikh':tarikh,

            })
        elif codes[0] == 'airplane':
            id=int(codes[1])
            seat=AirplaneSeat.objects.get(id= id)
            airplane=seat.airplane
            seat.full=False
            seat.save()
            airplane.capacity += 1
            Wanted_Airplane.objects.get(info=wanted_trip).delete()
            wanted_trip.delete()

            cost=airplane.cost

            account=int(cost-cost*0.05)
            gardesh=airplane.gardesh
            gardeshID = int(gardesh.id)
            gardeshgarID = int(gardeshgar.id)
            print(gardeshID)
            return  render(request, "tasviye_gardeshgar.html",{
                'account':account,
                'gardesh':gardesh,
                'gardeshID': gardeshID,
                'tarikh':tarikh,
                'gardeshgarID':gardeshgarID,
                'bankform':bankform,
                 'position':'زیر سامانه ی حسابداری',


            })

        elif codes[0] == 'train':
            id=int(codes[1])
            seat=TrainSeat.objects.get(id= id)
            train=seat.train
            seat.full=False
            seat.save()
            train.capacity += 1
            Wanted_Train.objects.get(info=wanted_trip).delete()
            wanted_trip.delete()

            cost=train.cost


            account=int(cost-cost*0.05)
            gardesh=train.gardesh
            gardeshID = int(gardesh.id)
            gardeshgarID = int(gardeshgar.id)
            print(gardeshID)
            return  render(request, "tasviye_gardeshgar.html",{
                'account':account,
                'gardesh':gardesh,
                'gardeshID': gardeshID,
                'tarikh':tarikh,
                'gardeshgarID':gardeshgarID,
                'bankform':bankform,
                 'position':'زیر سامانه ی حسابداری',
            })

        elif codes[0] == 'hotel':
            id=int(codes[1])
            seat=Room.objects.get(id= id)
            seat.full=False
            seat.save()
            Wanted_Hotel.objects.get(info=wanted_trip).delete()
            wanted_trip.delete()

            cost=seat.cost_perNight


            account=int(cost-cost*0.05)
            gardesh=seat.hotel.gardesh
            gardeshID = int(gardesh.id)
            gardeshgarID = int(gardeshgar.id)
            print(gardeshID)
            return  render(request, "tasviye_gardeshgar.html",{
                'account':account,
                'gardesh':gardesh,
                'gardeshID': gardeshID,
                'tarikh':tarikh,
                'gardeshgarID':gardeshgarID,
                'bankform':bankform,
                 'position':'زیر سامانه ی حسابداری',
            })

        elif codes[0] == 'restaurant':
                id=int(codes[1])
                seat=Table.objects.get(id= id)
                seat.full=False
                seat.save()
                Wanted_Restaurant.objects.get(info=wanted_trip).delete()
                wanted_trip.delete()

                cost=seat.cost_perClock


                account=int(cost-cost*0.05)
                gardesh=seat.restaurant.gardesh
                gardeshID = int(gardesh.id)
                gardeshgarID = int(gardeshgar.id)
                print(gardeshID)
                return  render(request, "tasviye_gardeshgar.html",{
                    'account':account,
                    'gardesh':gardesh,
                    'gardeshID': gardeshID,
                    'tarikh':tarikh,
                    'gardeshgarID':gardeshgarID,
                    'bankform':bankform,
                     'position':'زیر سامانه ی حسابداری',
                })

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

         wanted_trip.status='buy'
         wanted_trip.save()

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

         wanted_trip.status='buy'
         wanted_trip.save()

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
         wanted_trip.status='buy'
         wanted_trip.save()

         return render(request, "payment_bank.html",{
            'total_cost': total_cost,
            'train':train,
            'kind':'train',
         })
    elif codes[0]=='hotel':
         seat= Room.objects.get(id = int(codes[1]))
         hotel=seat.hotel
         total_cost=seat.cost_perNight

         wanted_trip.status='buy'
         wanted_trip.save()

         return render(request, "payment_bank_hotel.html",{
            'total_cost': total_cost,
            'hotel':hotel,
            'kind':'hotel',
            'ID':seat.id,
            'number':1,
         })

    elif codes[0]=='restaurant':
             seat= Table.objects.get(id = int(codes[1]))
             restaurant=seat.restaurant
             total_cost=seat.cost_perClock

             wanted_trip.status='buy'
             wanted_trip.save()

             return render(request, "payment_bank_restaurant.html",{
                'total_cost': total_cost,
                'restaurant':restaurant,
                'kind':'hotel',
                'ID':seat.id,
                'number':1,
             })
