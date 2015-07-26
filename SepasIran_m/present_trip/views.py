from django.shortcuts import render
from define_trip.models import *
def home(request , username = ''):
    return render(request, 'home.html', {'username':username})

def show_one_trip(request, kind = '' ,username = '' , id = ''):
    returned_dic = {}
    if request.method == "GET":
        returned_dic['kind'] = kind
        returned_dic['user'] = request.user
        returned_dic['username'] = 'username'
        if kind == 'service':
            return render(request , "one_trip.html", {'kind':kind , 'username':username})
        elif kind == 'tour':
            returned_dic['tour'] = Tour.objects.filter( id = id )[0]
            return render(request , "one_trip.html", returned_dic )
        elif kind == 'pack':
            return render(request , "one_trip.html", {'kind':kind , 'username':username})

    else:
        return None



def show_one_trip_status(request , kind = '' , username = ''):
    return render(request , "status_trip.html" , {'username':username , 'kind':kind})

def search(request , username = '' , ispack = ''):

    return render(request , "search_result.html" , {'username':username , 'ispack':ispack})

def start_search(request , username =''):
    return render(request,"search.html" , {'username':username})
# Create your views here.
