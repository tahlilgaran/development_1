from django.shortcuts import render
from define_trip.models import *
from accounting.models import *
from datetime import datetime
from buy_cancel.models import *
from user.models import *
from buy_cancel.forms import numberForm,peopleForm
from accounting.forms import bankForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseNotFound
import datetime
# Create your views here.
def paymentTour(request, tour_id=''):

    number=request.POST.get("number")
    tour= Tour.objects.get(id = tour_id)
    cost=tour.cost
    tarikh=datetime.datetime.now()
    total_cost=cost * int(number)
    gardesh = tour.gardesh
    first_name = request.POST.getlist("first_name")
    last_name = request.POST.getlist("last_name")
    melli_num =request.POST.getlist("melli_number")
    userm=request.user.userm
    user2=request.user
    gardeshgar=TouristProfile.objects.get(user =userm)

    if tour.capacity >= int(number):
            if tour.entire_capacity >= int(number):


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
                         'user2':user2,
                         'position':'زیر سامانه ی خرید',
                 'tarikh':tarikh,
             })

    return render(request, "payment_bank.html",{
        'total_cost': total_cost,
        'tour':tour,
        'kind':'tour',



    })


def confirmTour(request,tour_id=''):


        tour=Tour.objects.get(id = tour_id)
        user= request.user.userm
        user2=request.user
        sender= TouristProfile.objects.get(user = user)
        date = datetime.date.today()
        amount=request.POST.get("total_cost")
        gardesh=tour.gardesh
        number=int(int(amount)/tour.cost)
        tour.capacity=tour.capacity-number
        tour.entire_capacity=tour.entire_capacity-number
        tour.save()
        tarikh=datetime.datetime.now()

        info= Trans_info.objects.create(date=date,amount=int(amount),gardesh=gardesh)
        transaction = Trans_Kind1.objects.create(info=info,sender=sender)

        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'kind':'1',
            'user2':user2,
            'position':'زیر سامانه ی حسابداری',
            'tarikh':tarikh,
        })


def cancelTour(request , id=''):
    amount=request.POST.get("total_cost")
    tour=Tour.objects.get(id =id)
    number=int(int(amount)/tour.cost)
    user2=request.user
    tarikh=datetime.datetime.now()
    for i in range(number):

        Wanted_Trip.objects.last().delete()


    return render(request, "payment_cancel.html",{
        'user2':user2,
        'position':'زیر سامانه ی حسابداری',
        'tarikh':tarikh
    })

##################################################################################################
def paymentAirplane(request, airplane_id=''):
    tarikh=datetime.datetime.now()
    number=request.POST.get("number")
    user2=request.user
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
                i=0
                seats=AirplaneSeat.objects.filter(airplane = airplane ,full=False)

                for seat in seats:
                    if i == number:
                        break
                    else:
                        wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                                               first_name = first_name[i],last_name= last_name[i],
                                                               meli_code = melli_num[i],
                                                               peygiry_code = 'airplane'+'-'+str(seat.id)+'-'+request.user.username)
                        wantedairplane = Wanted_Airplane.objects.create(gardesh = seat ,info=wantedtrip);
                        i +=1

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
                         'user2':user2,
                         'position':'زیر سامانه ی خرید',
                 'tarikh':tarikh
             })

    return render(request, "payment_bank.html", {

        'total_cost':total_cost,
        'kind':'airplane',
        'airplane': airplane,
    })


def confirmAirplane(request,airplane_id=''):

        tarikh=datetime.datetime.now()
        airplane=AirPlane.objects.get(id = airplane_id)
        user= request.user.userm
        user2=request.user
        sender= TouristProfile.objects.get(user = user)
        date = datetime.date.today()
        amount=request.POST.get("total_cost")
        gardesh=airplane.gardesh
        number=int(amount)/airplane.cost
        airplane.capacity=airplane.capacity-number
        airplane.save()
        seats=AirplaneSeat.objects.filter(airplane =airplane,full=False)
        i=0
        for seat in seats:
            if i== number:
                break
            else:
                seat.full=True
                seat.save()
                i += 1
        info= Trans_info.objects.create(date=date,amount=int(amount),gardesh=gardesh)
        transaction = Trans_Kind1.objects.create(info=info,sender=sender)

        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'user2':user2,
            'position':'زیر سامانه ی حسابداری',
            'tarikh':tarikh,
        })

def cancelAirplane(request , id=''):
    amount=request.POST.get("total_cost")
    user2=request.user
    airplane=AirPlane.objects.get(id =id)
    number=int(int(amount)/airplane.cost)

    for i in range(number):

        Wanted_Trip.objects.last().delete()


    return render(request, "payment_cancel.html",{
        'user2':user2,
        'position':'زیر سامانه ی حسابداری',
    })

##############################TRAIN######################################################################################


def paymentTrain(request, train_id=''):
    tarikh=datetime.datetime.now()
    number=request.POST.get("number")
    train= Train.objects.get(id = train_id)
    cost=train.cost
    total_cost=cost * int(number)
    gardesh = train.gardesh
    user2=request.user
    first_name = request.POST.getlist("first_name")
    last_name = request.POST.getlist("last_name")
    melli_num =request.POST.getlist("melli_number")

    if train.capacity >= int(number):

                number=int(number)

                userm=request.user.userm
                gardeshgar=TouristProfile.objects.get(user =userm)
                i=0
                seats=TrainSeat.objects.filter(train= train ,full=False)

                for seat in seats:
                    if i == number:
                        break
                    else:
                        wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                                               first_name = first_name[i],last_name= last_name[i],
                                                               meli_code = melli_num[i],
                                                               peygiry_code = 'train'+'-'+str(seat.id)+'-'+request.user.username)
                        wantedtrain = Wanted_Train.objects.create(gardesh = seat ,info=wantedtrip);
                        i +=1

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
                         'user2':user2,
                        'position':'زیر سامانه ی خرید',
                 'tarikh':tarikh,
             })

    return render(request, "payment_bank.html",{
        'total_cost': total_cost,
        'kind':'train',
        'train':train,
    })



def confirmTrain(request,train_id=''):

        tarikh=datetime.datetime.now()
        train=Train.objects.get(id = train_id)
        user2=request.user
        user= request.user.userm
        sender= TouristProfile.objects.get(user = user)
        date = datetime.date.today()
        amount=request.POST.get("total_cost")
        gardesh=train.gardesh
        number=int(amount)/train.cost
        train.capacity=train.capacity-number
        train.save()
        seats=TrainSeat.objects.filter(train=train,full=False)
        i=0
        for seat in seats:
            if i== number:
                break
            else:
                seat.full=True
                seat.save()
                i += 1
        info= Trans_info.objects.create(date=date,amount=int(amount),gardesh=gardesh)
        transaction = Trans_Kind1.objects.create(info=info,sender=sender)

        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'user2':user2,
            'position':'زیر سامانه ی حسابداری',
            'tarikh':tarikh,
        })

def cancelTrain(request , id=''):
    tarikh=datetime.datetime.now()
    amount=request.POST.get("total_cost")
    user2=request.user
    train=Train.objects.get(id =id)
    number=int(int(amount)/train.cost)

    for i in range(number):

        Wanted_Trip.objects.last().delete()


    return render(request, "payment_cancel.html",{
        'user2':user2,
        'position':'زیر سامانه ی حسابداری',
    })

####################################RESTAURANT########################################################################
def paymentRestaurant(request,id=''):

    total_cost=request.POST.get("total_cost")
    restaurant= Restaurant.objects.get(id = id)


    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    melli_num =request.POST.get("melli_number")
    list= request.POST.get("ID")
    tableIDList=list.split(',')
    i=0
    for table in tableIDList:
       table=Table.objects.get(id = table)

       userm=request.user.userm
       gardeshgar=TouristProfile.objects.get(user =userm)
       wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                              first_name = first_name,last_name= last_name,
                                              meli_code = melli_num,
                                              peygiry_code = 'restuarant'+'-'+str(table.id)+'-'+request.user.username)
       wantedrestaurant = Wanted_Restaurant.objects.create(gardesh = table,info=wantedtrip);
       i += 1

    return render(request, "payment_bank_restaurant.html",{
        'total_cost': total_cost,
        'restaurant':restaurant,
        'ID':list,
        'number':i,
        'position':'زیر سامانه ی خرید',
    })



def confirmRestaurant(request,id=''):
        tarikh=datetime.datetime.now()
        restaurant=Restaurant.objects.get(id = id)
        user= request.user.userm
        sender= TouristProfile.objects.get(user = user)
        date = datetime.date.today()
        number=request.POST.get("number")
        list= request.POST.get("ID")
        tableIDList=list.split(',')
        user2=request.user
        for t in tableIDList:
            table=Table.objects.get(id = t)
            table.full=True
            table.save()
            info= Trans_info.objects.create(date=date,amount=int(table.cost_perClock),gardesh=restaurant.gardesh)
            transaction = Trans_Kind1.objects.create(info=info,sender=sender)

        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'user2':user2,
            'position':'زیر سامانه ی حسابداری',
            'tarikh':tarikh,
        })



def cancelRestaurant(request , id=''):
    user2=request.user
    number=int(request.POST.get("number"))
    for i in range(number):
        Wanted_Trip.objects.last().delete()

    return render(request, "payment_cancel.html",{
        'user2':user2,
        'position':'زیر سامانه ی حسابداری',
    })

##################################HOTEL###############################################################################

def paymentHotel(request,id=''):
    total_cost=request.POST.get("total_cost")
    hotel= Hotel.objects.get(id = id)

    tarikh=datetime.datetime.now()
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    melli_num =request.POST.get("melli_number")
    list= request.POST.get("ID")
    roomIDList=list.split(',')
    i=0
    for r in roomIDList:
       room=Room.objects.get(id = r)

       userm=request.user.userm
       gardeshgar=TouristProfile.objects.get(user =userm)
       wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='buy',
                                              first_name = first_name,last_name= last_name,
                                              meli_code = melli_num,
                                              peygiry_code = 'hotel'+'-'+str(room.id)+'-'+request.user.username)
       wantedrestaurant = Wanted_Hotel.objects.create(gardesh = room,info=wantedtrip);
       i += 1

    return render(request, "payment_bank_hotel.html",{
        'total_cost': total_cost,
        'hotel':hotel,
        'ID':list,
        'number':i,
        'tarikh':tarikh,
    })


    
def confirmHotel(request,id=''):
        hotel=Hotel.objects.get(id = id)
        user= request.user.userm
        sender= TouristProfile.objects.get(user = user)
        date = datetime.date.today()
        tarikh=datetime.datetime.now()
        list= request.POST.get("ID")
        roomIDList=list.split(',')
        user2=request.user
        for t in roomIDList:
            room=Room.objects.get(id = t)
            room.full=True
            room.save()
            info= Trans_info.objects.create(date=date,amount=int(room.cost_perNight),gardesh=hotel.gardesh)
            transaction = Trans_Kind1.objects.create(info=info,sender=sender)

        return render(request, "transaction-status.html",{
            'transaction':transaction,
            'user2':user2,
            'position':'زیر سامانه ی حسابداری',
            'tarikh':tarikh

        })

def cancelHotel(request , id=''):
    user2=request.user

    number=int(request.POST.get("number"))
    for i in range(number):
        Wanted_Trip.objects.last().delete()

    return render(request, "payment_cancel.html",{
        'user2':user2,
        'position':'زیر سامانه ی حسابداری',
    })

#####################################################################################################################
def ozviyat(request,username=''):

    return render(request, "payment_ozviyat.html",{
        'total_cost':'۵۰۰۰',
        'username':username,
    })
def confirmOzv(request,username=''):
    tarikh=datetime.datetime.now()
    user=User.objects.get(username= username)

    userm=user.userm
    y=TouristProfile.objects.get(user= userm)
    y.has_payed=True
    y.save()
    return render(request, "transaction-status.html",{
        'tarikh':tarikh,
        'user2':user,
        'position':'زیر سامانه ی  حسابداری',

    })
########################################################################################################

def tasviye(request):
    tarikh=datetime.datetime.now()
    userm =request.user.userm
    user = TouristProfile.objects.get(user= userm)
    account= user.account
    intaccount=int(account)
    user2=request.user
    bankform=bankForm(request.POST)
    if intaccount == 0:
        return render(request, "tasviye_gardeshgar.html",{
            'zero':True,
            'tarikh':tarikh
        })
    else :
        return  render(request, "tasviye_gardeshgar.html",{
            'zero':False,
            'user': request.user,
            'account': intaccount,
            'bankform':bankForm,
            'user2':user2,
            'position':'زیر سامانه ی  حسابداری',
            'tarikh':tarikh,
        })


def tasviyeConfirm(request):
    tarikh=datetime.datetime.now()
    date = datetime.date.today()
    gardeshID=int(request.POST.get("gardeshID"))
    account=int(request.POST.get("account"))
    gardeshgarID=int(request.POST.get("gardeshgarID"))
    print(gardeshID)
    print(account)
    user2=request.user
    gardesh=Gardesh.objects.get(id= gardeshID)
    receiver=TouristProfile.objects.get( id = gardeshgarID)
    info= Trans_info.objects.create(date=date,amount=account,gardesh=gardesh)
    transaction = Trans_Kind3.objects.create(info=info,receiver=receiver)

    return HttpResponseRedirect('/userpage/',{
        'user2':user2,
        'position':'زیر سامانه ی  حسابداری',
        'tarikh':tarikh,
    })

def tasviyeConfirm2(request):
    tarikh=datetime.datetime.now()
    date = datetime.date.today()
    gardeshID=int(request.POST.get("gardeshID"))
    account=int(request.POST.get("final"))

    user2=request.user
    gardesh=Gardesh.objects.get(id= gardeshID)
    receiver=TourBuilderProfile.objects.get( user=request.user.userm)
    info= Trans_info.objects.create(date=date,amount=account,gardesh=gardesh)
    transaction = Trans_Kind2.objects.create(info=info,receiver=receiver)

    return HttpResponseRedirect('/userpage/',{
        'user2':user2,
        'position':'زیر سامانه ی  حسابداری',
        'tarikh':tarikh,
    })

############################################################################################################
def tasviyeGar(request):
    user=request.user
    userm=user.userm
    tarikh=datetime.datetime.now()
    if user.userm.kind == 'gardeshgar':
        return HttpResponseNotFound()
    else:
        date=datetime.datetime.now()
        builderP=TourBuilderProfile.objects.get(user=userm)

        gardesh=Gardesh.objects.filter(builder=builderP,)
        return render(request, "tasviye_gardeshsaz.html",{
            'gardesh':gardesh,
            'user2':user,
            'position':'زیر سامانه ی  حسابداری',
            'tarikh':tarikh
        })
def tasviyeID(request,id=''):
    date=datetime.datetime.now()
    tarikh=datetime.datetime.now()
    gardesh= Gardesh.objects.get(id =id)
    agree=gardesh.agreement
    percent=agree.percent
    user= request.user
    trans=Trans_info.objects.filter(date__lt=date,gardesh= gardesh)
    if not trans:
        return render(request,"nothing.html",{
            'position':'زیر سامانه ی  حسابداری',
            'user2':user,
            'tarikh':tarikh,
        })
    total=0
    for tr in trans:
        total +=int( tr.amount)

    final= int(total-total*percent)
    bankform=bankForm()
    return render(request,"tasviye_gardeshsaz2.html",{

        'final':final,
        'bankform':bankform,
        'position':'زیر سامانه ی  حسابداری',
        'user2':user,
        'tarikh':tarikh,
        'gardeshID':gardesh.id,


    })