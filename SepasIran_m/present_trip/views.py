from django.shortcuts import render
from define_trip.models import *
from buy_cancel.models import *
from django.http import Http404
import datetime

def home(request , username = ''):
    return render(request, 'home.html', {'username':username})

def show_one_trip(request, kind = ''  , id = 0):
    returned_dic = {}
    if request.method == "GET":
        returned_dic['kind'] = kind
        returned_dic['user'] = request.user
        # returned_dic['username'] = 'username'
        trip =''
        pic_list = []
        pic_q = ''

        if kind == 'tour':
            trip = Tour.objects.filter(id = id)[0]
            pic_q = Picture.objects.filter(gardesh = trip.gardesh)

        elif kind == 'hotel':
            trip = Hotel.objects.filter(id = id)[0]
            pic_q = Picture.objects.filter(gardesh = trip.gardesh)
            rooms = Room.objects.filter(hotel = trip)
            returned_dic['rooms'] = rooms #TODO: room haro ba tavajoh be voroodi neshoon bede.

        elif kind == 'restaurant':
            trip = Restaurant.objects.filter(id = id)[0]
            pic_q = Picture.objects.filter(gardesh = trip.gardesh)
            tables = Table.objects.filter(restaurant = trip)
            print(tables)
            returned_dic['tables'] = tables

        elif kind == 'airplane':
            trip = AirPlane.objects.filter(id = id)[0]
            pic_q = Picture.objects.filter(gardesh = trip.gardesh)

        elif kind == 'train':
            trip = Train.objects.filter(id = id)[0]
            pic_q = Picture.objects.filter(gardesh = trip.gardesh)

        elif kind == 'pack':
            return render(request , "one_trip.html", {'kind':kind})


        if not pic_q:
            pic_list.append(trip.gardesh.builder.user.picture)
        else:
            for i in pic_q:
                pic_list.append(i.picture)
        returned_dic['trip'] = trip
        returned_dic['pic_list'] = pic_list
        returned_dic['pic_range'] = range(0,pic_list.__len__())
        return render(request,"one_trip.html" , returned_dic)

    else:
        return None



def show_one_trip_status(request , kind = '', id = 0 , sub_number = 0):
    return_dic = {}
    trip = ''
    html_file = ''
    sub_trip = ''
    user_kind = request.user.userm.kind
    if (user_kind == 'gardeshsaz'):
        builder = request.user.userm.bprofile
    elif(user_kind == 'manager'):
        builder = request.userm.mprofile
    else:
        builder = ''
    if request.method == 'GET':
        print (builder)
        now = datetime.datetime.now()
        future_ten_days = [now , now + datetime.timedelta(days=10)]
        if kind == 'tour':
            trip = Tour.objects.filter(id = id)[0]
            html_file = 'status_tour.html'
            if trip.gardesh.builder == builder or builder.user.kind == 'manager':
                buy_trips = Wanted_Tour.objects.filter(gardesh = trip , info__status = 'buy')
                reserve_trip = Wanted_Tour.objects.filter(gardesh = trip , info__status = 'reserve')
                zarfiat = trip.capacity - buy_trips.__len__() - reserve_trip.__len__()


        if kind == 'restaurant':#todo: nahve ye namayesh bayad behtar beshe.
            trip = Restaurant.objects.filter(id = id)[0]
            html_file = 'status_tour.html'
            if trip.gardesh.builder == builder or builder.user.kind == 'manager':
                sub_trip = Table.objects.filter(number = sub_number , restaurant = trip)[0]
                buy_trips = Wanted_Restaurant.objects.filter(gardesh = sub_trip , gardesh__date = datetime.datetime.today() , info__status = 'buy')
                reserve_trip = Wanted_Restaurant.objects.filter(gardesh = sub_trip, gardesh__date = datetime.datetime.today() , info__status = 'reserve')
                zarfiat = -1

        if kind == 'hotel':#todo: nahve namayesheshoon bayad behtar beshe. :|
            trip = Hotel.objects.filter(id = id)[0]
            html_file = 'status_tour.html'
            if trip.gardesh.builder == builder or builder.user.kind == 'manager':
                sub_trip = Room.objects.filter(number = sub_number , hotel = trip)[0]
                buy_trips = Wanted_Hotel.objects.filter(gardesh = sub_trip ,gardesh__date__range = future_ten_days, info__status = 'buy')
                reserve_trip = Wanted_Hotel.objects.filter(gardesh = sub_trip ,gardesh__date__range = future_ten_days, info__status = 'reserve')
                zarfiat = -1

        if kind == 'airplane':
            trip = AirPlane.objects.filter(id = id )[0]
            html_file = 'status_tour.html'
            if trip.gardesh.builder == builder or builder.user.kind == 'manager':
                buy_trips = Wanted_Airplane.objects.filter(gardesh__airplane = trip , info__status = 'buy')
                reserve_trip = Wanted_Airplane.objects.filter(gardesh__airplane = trip , info__status = 'reserve')
                zarfiat = trip.capacity - buy_trips.__len__() - reserve_trip.__len__()

        if kind == 'train':
            trip = Train.objects.filter(id = id )[0]
            html_file = 'status_tour.html'
            if trip.gardesh.builder == builder or builder.user.kind == 'manager':
                buy_trips = Wanted_Train.objects.filter(gardesh__train = trip , info__status = 'buy')
                reserve_trip = Wanted_Train.objects.filter(gardesh__train = trip , info__status = 'reserve')
                zarfiat = trip.capacity - buy_trips.__len__() - reserve_trip.__len__()
        # else:
        #     raise Http404("Page not found")

        if trip.gardesh.builder == builder or user_kind == 'manager':
            return_dic['builder'] = trip.gardesh.builder
            print(trip)
            return_dic['trip'] = trip
            return_dic['buy_trips'] = buy_trips
            return_dic['reserve_trip'] = reserve_trip
            return_dic['zarfiat'] = zarfiat
            return_dic['sub_trip'] = sub_trip
        else:
            return_dic['error'] = 'نمایش وضعیت گردش به گردشساز آن گردش امکان پذیر است.'

        return render(request , html_file , return_dic)
    else:
        return None





def search(request , username = '' , ispack = ''):

    return render(request , "search_result.html" , {'username':username , 'ispack':ispack})

def start_search(request , username =''):
    return render(request,"search.html" , {'username':username})
# Create your views here.
