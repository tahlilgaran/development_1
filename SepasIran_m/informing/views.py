import datetime
import time
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from define_trip.models import Train,Tour,AirPlane,Room,Table
from buy_cancel.models import Wanted_Trip
@login_required()
def account(requst):
    if requst.method == 'GET':
        now = datetime.datetime.now()
        future_ten_day = [now , now + datetime.timedelta(days=10)]
        returned_dic = {}
        user_kind = requst.user.userm.kind
        returned_dic['user_kind'] = user_kind
        if user_kind == 'manager':
            return redirect("/manager/Dashboard")
        elif user_kind == 'gardeshgar':
            user = requst.user.userm.tprofile # gardeshgar
            gardeshgar_list = Wanted_Trip.objects.filter(gardeshgar = user)[:10]
            returned_dic['gardeshgar_list'] = gardeshgar_list
        elif user_kind == 'gardeshsaz':
            user = requst.user.userm.bprofile # gardeshsaz
            tour_list = Tour.objects.filter(gardesh__builder = user , start__range = future_ten_day)
            hotel_list = Room.objects.filter(hotel__gardesh__builder = user , date__range = future_ten_day)
            airplane_list = AirPlane.objects.filter(gardesh__builder = user , start__range = future_ten_day)
            train_list = Train.objects.filter(gardesh__builder = user , start__range = future_ten_day)
            restaurant_list = Table.objects.filter(restaurant__gardesh__builder = user , date__range = future_ten_day)
            returned_dic['tour_list'] = tour_list
            returned_dic['hotel_list'] = hotel_list
            returned_dic['airplane_list'] = airplane_list
            returned_dic['train_list'] = train_list
            returned_dic['restaurant_list'] = restaurant_list

        else:
            raise Http404("Page not found")
        print(user_kind)
        returned_dic['user'] = user
        return render(requst , 'account.html' , returned_dic)
    else:
        return None

