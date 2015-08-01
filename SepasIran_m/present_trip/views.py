from django.shortcuts import render
from define_trip.models import *
from buy_cancel.models import *
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



def show_one_trip_status(request , kind = '', id = 0 , sub_kind = '' , sub_id = 0):
    return_dic = {}
    trip = ''
    html_file = ''
    builder = request.user.userm.bprofile
    return_dic['builder'] = builder
    if request.method == 'GET':
        if kind == 'tour':
            trip = Tour.objects.filter(id = id)[0]
            html_file = 'status_tour.html'
            if trip.gardesh.builder == builder:
                buy_trips = Wanted_Tour.objects.filter(gardesh = trip , info__status = 'buy')
                reserve_trip = Wanted_Tour.objects.filter(gardesh = trip , info__status = 'reserve')
                zarfiat = trip.capacity - buy_trips.__len__() - reserve_trip.__len__()


        if kind == 'restaurant':
            trip = Restaurant.objects.filter(id = id)[0]
            html_file = 'status_restaurant.html'
            if trip.gardesh.builder == builder:
                wanted_trip = Wanted_Restaurant.objects.filter(gardesh = trip)

        if kind == 'hotel':
            trip = Hotel.objects.filter(id = id)[0]
            html_file = 'status_hotel.html'
            if trip.gardesh.builder == builder:
                wanted_trip = Wanted_Hotel.objects.filter(gardesh = trip)

        if kind == 'airplane':
            trip = AirPlane.objects.filter(id = id )[0]
            html_file = 'status_tour.html'
            if trip.gardesh.builder == builder:
                buy_trips = Wanted_Airplane.objects.filter(gardesh__airplane = trip , info__status = 'buy')
                reserve_trip = Wanted_Airplane.objects.filter(gardesh__airplane = trip , info__status = 'reserve')
                zarfiat = trip.capacity - buy_trips.__len__() - reserve_trip.__len__()

        if kind == 'train':
            trip = Train.objects.filter(id = id )[0]
            html_file = 'status_tour.html'
            if trip.gardesh.builder == builder:
                buy_trips = Wanted_Train.objects.filter(gardesh__train = trip , info__status = 'buy')
                reserve_trip = Wanted_Train.objects.filter(gardesh__train = trip , info__status = 'reserve')
                zarfiat = trip.capacity - buy_trips.__len__() - reserve_trip.__len__()

        if trip.gardesh.builder != builder:
            return_dic['error'] = 'نمایش وضعیت گردش به گردشساز آن گردش امکان پذیر است.'
        else:
            # print(trip.gardesh.name)
            return_dic['trip'] = trip
            return_dic['buy_trips'] = buy_trips
            return_dic['reserve_trip'] = reserve_trip
            return_dic['zarfiat'] = zarfiat
        return render(request , html_file , return_dic)
    else:
        return None





def search(request , username = '' , ispack = ''):

    return render(request , "search_result.html" , {'username':username , 'ispack':ispack})

def start_search(request , username =''):
    return render(request,"search.html" , {'username':username})
# Create your views here.
