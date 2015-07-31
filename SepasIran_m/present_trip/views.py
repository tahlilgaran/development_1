from django.shortcuts import render
from define_trip.models import *
def home(request , username = ''):
    return render(request, 'home.html', {'username':username})

def show_one_trip(request, kind = ''  , id = 0):
    # print("tourist_profile: {}".format(request.user.userm.kind))
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
            returned_dic['tables'] = tables

        elif kind == 'airplane':
            trip = AirPlane.objects.filter(id = id)
            pic_q = Picture.objects.filter(gardesh = trip.gardesh)

        elif kind == 'train':
            trip = Train.objects.filter(id = id)
            pic_q = Picture.objects.filter(gardesh = trip)

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



def show_one_trip_status(request , kind = '' , username = ''):
    return render(request , "status_trip.html" , {'username':username , 'kind':kind})

def search(request , username = '' , ispack = ''):

    return render(request , "search_result.html" , {'username':username , 'ispack':ispack})

def start_search(request , username =''):
    return render(request,"search.html" , {'username':username})
# Create your views here.
