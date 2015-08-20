import datetime
import time
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from define_trip.models import Train,Tour,AirPlane,Room,Table,Restaurant,Hotel
from buy_cancel.models import Wanted_Trip,Wanted_Tour,Wanted_Train,Wanted_Hotel,Wanted_Restaurant,Wanted_Airplane

tarikh = datetime.datetime.now()
@login_required()
def account(requst):
    returned_dic = {}
    returned_dic['user2'] = requst.user
    returned_dic['position'] = 'سامانه اطلاع رسانی و تقویم - صفحه ی کاربری'
    returned_dic['tarikh'] = tarikh
    
    if requst.method == 'GET':
        now = datetime.datetime.now()
        future_ten_day = [now + datetime.timedelta(days = 1) , now + datetime.timedelta(days=10)]
        last_ten_day = [now - datetime.timedelta(days = 10) , now]
        user_kind = requst.user.userm.kind
        returned_dic['user_kind'] = user_kind


        if user_kind == 'manager':
            return redirect("/manager/Dashboard")

        elif user_kind == 'gardeshgar':
            user = requst.user.userm.tprofile # gardeshgar

            tour_list_all = Wanted_Tour.objects.filter(info__gardeshgar = user , gardesh__start__range = future_ten_day)
            tour_list = []
            for item in tour_list_all:
                if not item.gardesh in tour_list:
                    tour_list.append(item.gardesh)

            airplane_list_all = Wanted_Airplane.objects.filter(info__gardeshgar = user, gardesh__airplane__start__range = future_ten_day)
            airplane_list=[]
            for item in airplane_list_all:
                if not item.gardesh.airplane in airplane_list:
                    airplane_list.append(item.gardesh.airplane)

            train_list_all = Wanted_Train.objects.filter(info__gardeshgar = user, gardesh__train__start__range = future_ten_day)
            train_list = []
            for item in train_list_all:
                if not item.gardesh.train in train_list:
                    train_list.append(item.gardesh.train)

            hotel_list_all = Wanted_Hotel.objects.filter(info__gardeshgar = user , gardesh__date__range = future_ten_day)
            hotel_list = []
            for item in hotel_list_all:
                if not item.gardesh.hotel in hotel_list:
                    hotel_list.append(item.gardesh.hotel)

            restaurant_list_all = Wanted_Restaurant.objects.filter(info__gardeshgar = user, gardesh__date__range = future_ten_day)
            print (restaurant_list_all)
            restaurant_list = []
            for item in restaurant_list_all:
                if not item.gardesh.restaurant in restaurant_list:
                    restaurant_list.append(item.gardesh.restaurant)

            returned_dic['tour_list'] = tour_list
            returned_dic['hotel_list'] = hotel_list
            returned_dic['airplane_list'] = airplane_list
            returned_dic['train_list'] = train_list
            returned_dic['restaurant_list'] = restaurant_list

            returned_dic['tour_list_all'] = tour_list_all
            returned_dic['hotel_list_all'] = hotel_list_all
            returned_dic['airplane_list_all'] = airplane_list_all
            returned_dic['train_list_all'] = train_list_all
            returned_dic['restaurant_list_all'] = restaurant_list_all
            returned_dic['user'] = user


            # current_trip:
            current_tour_all = Wanted_Tour.objects.filter(info__gardeshgar = user , gardesh__start__lte = now , gardesh__end__gte = now)
            current_tour = []
            for item in current_tour_all:
                if not item.gardesh in current_tour:
                    current_tour.append(item.gardesh)

            returned_dic['current_tour'] = current_tour
            returned_dic['current_tour_all'] = current_tour_all

            #last_trip
            last_tour_all = Wanted_Tour.objects.filter(info__gardeshgar = user , gardesh__end__range = last_ten_day)
            last_tour = []
            for item in last_tour_all:
                if not item.gardesh in last_tour:
                    last_tour.append(item.gardesh)

            returned_dic['last_tour'] = last_tour
            returned_dic['last_tour_all'] = last_tour_all

            #takhfifi
            free_tour = Tour.objects.filter(start__range = future_ten_day).exclude(gardesh__free = 0)
            returned_dic['free_tour'] = free_tour



            return render(requst , 'gardeshgar_account.html' , returned_dic)


        elif user_kind == 'gardeshsaz':
            user = requst.user.userm.bprofile # gardeshsaz
            tour_list = Tour.objects.filter(gardesh__builder = user , start__range = future_ten_day)
            hotel_list = Hotel.objects.filter(gardesh__builder = user)
            airplane_list = AirPlane.objects.filter(gardesh__builder = user , start__range = future_ten_day)
            train_list = Train.objects.filter(gardesh__builder = user , start__range = future_ten_day)
            restaurant_list = Restaurant.objects.filter(gardesh__builder = user)
            returned_dic['tour_list'] = tour_list
            returned_dic['hotel_list'] = hotel_list
            returned_dic['airplane_list'] = airplane_list
            returned_dic['train_list'] = train_list
            returned_dic['restaurant_list'] = restaurant_list
            returned_dic['user'] = user

            return render(requst , 'gardeshsaz_account.html' , returned_dic)

        else:
            raise Http404("Page not found")

    else:
        return None

