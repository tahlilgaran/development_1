from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from datetime import timedelta, date
from .forms import *
from user.models import TourBuilderProfile,UserM
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def tarif_kind(request):
    date = datetime.datetime.now()
    position = 'تعریف خدمت'
    username = ''
    u1 = request.user
    if UserM.objects.filter(user = u1):
        muser = UserM.objects.filter(user = u1)[0]
        if muser.kind == 'gardeshsaz':
            username = 'gardeshsaz'

    if request.POST.get("next","") != "":
        print(request.POST.get("optradio"))
        if request.POST.get("optradio")== '1' :
            return HttpResponseRedirect('/tourdefine/hotel/')
        elif request.POST.get("optradio")== '2':
            return HttpResponseRedirect('/tourdefine/restaurant/')
        elif request.POST.get("optradio")== '3':
            return HttpResponseRedirect('/tourdefine/airplane/')
        elif request.POST.get("optradio")== '4':
            return HttpResponseRedirect('/tourdefine/train/')

    if request.POST.get("cancel","") != "":
        return HttpResponseRedirect('/userpage/')

    return  render(request,"tarif_kind.html",{
         'username': username,
         'user2':u1,
        'position':position,
         'tarikh':date,
    })

@login_required()
def tour_define_2(request,id):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'تعریف تور> ورود اطلاعات> تایید اطلاعات'
    gardesh = Gardesh.objects.get(id = id)
    tour = Tour.objects.get(gardesh = gardesh)
    if request.POST.get("return","") != "":
        tour.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/tour/')
    if request.POST.get("cancel","") != "":
        tour.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/userpage/')

    return render(request, "tour_define_2.html",{
        'gardesh': gardesh,
        'tour': tour,
        'username':"gardeshsaz",
        'user2':user2,
        'position':position,
        'tarikh':date,
    })

@login_required()
def tour_define(request):
    date = datetime.datetime.now()
    username = ''
    builder = ''
    position = 'تعریف تور> ورود اطلاعات'
    u1 = request.user
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)


    if request.POST.get("save","") != "":
        form = TourForm(request.POST,request.FILES)

        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = form.cleaned_data['name']
            gardesh.builder = builder
            gardesh.kind = 'tour'
            a = Agreement()
            a.kind ='tr-g'
            a.percent = '10'
            a.save()
            gardesh.agreement = a
            gardesh.degree = 'G'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if request.POST.get('other_explain'):
                gardesh.other_explain = request.POST.get('other_explain')
                print(gardesh.other_explain)
            gardesh.save()
            if form.cleaned_data['pic1']:
                pic1 = Picture()
                pic1.picture = form.cleaned_data['pic1']
                pic1.gardesh = gardesh
                pic1.save()
            if form.cleaned_data['pic2']:
                pic2 = Picture()
                pic2.picture = form.cleaned_data['pic2']
                pic2.gardesh = gardesh
                pic2.save()
            if form.cleaned_data['pic3']:
                pic3 = Picture()
                pic3.picture = form.cleaned_data['pic3']
                pic3.gardesh = gardesh
                pic3.save()
            if form.cleaned_data['pic4']:
                pic4 = Picture()
                pic4.picture = form.cleaned_data['pic4']
                pic4.gardesh = gardesh
                pic4.save()

            print(request.POST.get("rt"))
            if request.POST.get("rt") == '1':
                t = TransferDevice()
                print(t.id)
                t.name = form.cleaned_data['airplane']
                print(t.name)
                t.degree = "G"
                t.kind = "A"
                t.save()
                f.transfer_device = t
            elif request.POST.get("rt") == '2':
                t = TransferDevice()
                t.name = form.cleaned_data['train']
                print(t.name)
                t.degree = "S"
                t.kind = "T"
                t.save()
                f.transfer_device = t
            elif request.POST.get("rt") == '3':
                t = TransferDevice()
                t.name = form.cleaned_data['bus']
                print(t.name)
                t.degree = "B"
                t.kind = "B"
                t.save()
                f.transfer_device = t

            print(request.POST.get("rm"))
            if request.POST.get("rm") == '1':
                l = Location()
                print(l.id)
                l.name = form.cleaned_data['hotel']
                l.kind = 'H'
                l.degree = 'G'
                l.save()
                f.stay_location = l
            elif request.POST.get("rm") == '2':
                l = Location()
                l.name = form.cleaned_data['apartment']
                l.kind = 'A'
                l.degree = 'S'
                l.save()
                f.stay_location = l
            elif request.POST.get("rm") == '3':
                l = Location()
                l.name = form.cleaned_data['mosaferkhane']
                l.kind = 'M'
                l.degree = 'B'
                l.save()
                f.stay_location = l

            if f.stay_location.degree == 'G':
                if f.transfer_device.degree != 'B':
                    gardesh.degree = 'G'
                else:
                    gardesh.degree = 'S'

            if f.stay_location.degree == 'S':
                if f.transfer_device.degree != 'B':
                    gardesh.degree = 'S'
                else:
                    gardesh.degree = 'B'

            if f.stay_location.degree == 'B':
                if f.transfer_device.degree == 'G':
                    gardesh.degree = 'S'
                else:
                    gardesh.degree = 'B'

            gardesh.save()
            f.start = form.cleaned_data['start']
            f.end = form.cleaned_data['end']
            f.gardesh = gardesh
            f.save()
            u = gardesh.id
            return HttpResponseRedirect('/tourdefine/tour/2/'+ str(u))

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = TourForm()

    return render(request,"tour_define.html",{
        'username': username,
        'form': form,
        'b': builder,
        'user2':u1,
        'position':position,
        'tarikh':date,
    })

@login_required()
def airplane_define(request):
    date = datetime.datetime.now()
    username = ''
    builder = ''
    u1 = request.user
    position = 'تعریف خدمت>تعریف پرواز'
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)


    if request.POST.get("save","") != "":
        form = AirPlaneForm(request.POST)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = form.cleaned_data['name']
            gardesh.builder = builder
            gardesh.kind = 'airplane'
            a = Agreement()
            a.kind ='a-g'
            a.percent = '10'
            a.save()
            gardesh.agreement = a
            gardesh.degree = 'g'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if request.POST.get('other_explain'):
                gardesh.other_explain = request.POST.get('other_explain')
                print(gardesh.other_explain)

            gardesh.save()
            f.gardesh = gardesh
            f.start = form.cleaned_data['start']
            f.save()
            num = request.POST.get('number')
            print(num)
            ran = range(1,int(num))
            capa = 0
            for i in ran :
                start = request.POST.get('s'+str(i))
                end = request.POST.get('e'+str(i))
                ran2 = range(int(start),int(end)+1)
                for j in ran2:
                    seat = AirplaneSeat()
                    seat.number = j
                    seat.airplane = f
                    seat.save()
                    capa += 1
            f.capacity = capa
            f.save()

            return HttpResponseRedirect('/tourdefine/airplane/2/'+ str(gardesh.id))

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = AirPlaneForm()

    return render(request,"airplane_define.html",{
        'username': username,
        'form': form,
        'b': builder,
        'user2':u1,
        'position':position,
        'tarikh':date,
    })

@login_required()
def airplane_define_2(request,id):
    date = datetime.datetime.now()
    gardesh = Gardesh.objects.get(id = id)
    airplane = AirPlane.objects.get(gardesh = gardesh)
    user2 = request.user
    position = 'تعریف خدمت> تعریف پرواز> تایید اطلاعات پرواز'

    if request.POST.get("return","") != "":
        airplane.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/airplane/')
    if request.POST.get("cancel","") != "":
        airplane.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/userpage/')

    return render(request, "airplane_define_2.html",{
        'gardesh': gardesh,
        'airplane': airplane,
        'username':"gardeshsaz",
        'user2': user2,
        'position': position,
        'tarikh':date,
    })

@login_required()
def train_define(request):
    date = datetime.datetime.now()
    username = ''
    builder = ''
    u1 = request.user
    position = 'تعریف خدمت> تعریف قطار'
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)


    if request.POST.get("save","") != "":
        form = TrainForm(request.POST)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = form.cleaned_data['name']
            gardesh.builder = builder
            gardesh.kind = 'train'
            a = Agreement()
            a.kind ='t-s'
            a.percent = '8'
            a.save()
            gardesh.agreement = a
            gardesh.degree = 'S'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if request.POST.get('other_explain'):
                gardesh.other_explain = request.POST.get('other_explain')
                print(gardesh.other_explain)
            gardesh.save()
            f.gardesh = gardesh
            f.start = form.cleaned_data['start']
            f.save()
            num = request.POST.get('number')
            ran = range(1,int(num))
            capa = 0
            for i in ran :
                if request.POST.get('s'+str(i))!="" and request.POST.get('e'+str(i))!="":
                    start = request.POST.get('s'+str(i))
                    end = request.POST.get('e'+str(i))
                    print(str(i)+'s')
                    ran2 = range(int(start),int(end)+1)
                    print(str(i)+'p')
                    for j in ran2:
                        seat = TrainSeat()
                        seat.number = j
                        seat.train = f
                        seat.save()
                        capa += 1
            f.capacity = capa
            f.save()
            return HttpResponseRedirect('/tourdefine/train/2/'+str(gardesh.id))

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = TrainForm()

    return render(request,"train_define.html",{
        'username': username,
        'form': form,
        'b': builder,
        'user2': u1,
        'position': position,
        'tarikh':date,
    })


@login_required()
def train_define_2(request,id):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'تعریف خدمت> تعریف قطار> ورود اطلاعات> تایید اطلاعات'
    gardesh = Gardesh.objects.get(id = id)
    train = Train.objects.get(gardesh = gardesh)
    if request.POST.get("return","") != "":
        train.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/train/')
    if request.POST.get("cancel","") != "":
        train.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/userpage/')

    return render(request, "train_define_2.html",{
        'gardesh': gardesh,
        'train': train,
        'username':"gardeshsaz",
        'user2': user2,
        'position': position,
        'tarikh':date,
    })

@login_required()
def hotel_define_first(request):
    date = datetime.datetime.now()
    u1 = request.user
    position = 'لیست هتل ها'
    username = ''
    builder = ''
    names = []
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)
                gardeshs = Gardesh.objects.filter(builder = builder)
                for g in gardeshs:
                    if g.kind == 'hotel':
                        names += [g.name]

    if request.POST.get("define","") != "":
        return HttpResponseRedirect('/tourdefine/hotel/define/')

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')

    return render(request,"hotel_define_1.html",{
        'username': username,
        'b': builder,
        'user2': u1,
        'position': position,
        'names': names,
        'tarikh':date,
    })

@login_required()
def hotel_define(request):
    date = datetime.datetime.now()
    username = ''
    builder = ''
    u1 = request.user
    position = 'تعریف یک هتل'
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)

    if request.POST.get("save","") != "":
        form = HotelForm(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = form.cleaned_data['name']
            gardesh.builder = builder
            gardesh.kind = 'hotel'
            a = Agreement()
            a.kind ='h-g'
            a.percent = '10'
            a.save()
            gardesh.agreement = a
            gardesh.degree = 'G'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if request.POST.get('other_explain'):
                gardesh.other_explain = request.POST.get('other_explain')
                print(gardesh.other_explain)
            gardesh.save()
            f.gardesh = gardesh
            if form.cleaned_data['pic1']:
                pic1 = Picture()
                pic1.picture = form.cleaned_data['pic1']
                pic1.gardesh = gardesh
                pic1.save()
            if form.cleaned_data['pic2']:
                pic2 = Picture()
                pic2.picture = form.cleaned_data['pic2']
                pic2.gardesh = gardesh
                pic2.save()
            if form.cleaned_data['pic3']:
                pic3 = Picture()
                pic3.picture = form.cleaned_data['pic3']
                pic3.gardesh = gardesh
                pic3.save()
            if form.cleaned_data['pic4']:
                pic4 = Picture()
                pic4.picture = form.cleaned_data['pic4']
                pic4.gardesh = gardesh
                pic4.save()
            if request.POST.get('address'):
                f.address = request.POST.get('address')
            f.save()
            return HttpResponseRedirect('/tourdefine/hotel/2/'+str(gardesh.id))

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = HotelForm()

    return render(request,"hotel_define.html",{
        'username': username,
        'form': form,
        'b': builder,
        'user2':u1,
        'position':position,
        'tarikh':date,
    })

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

@login_required()
def hotel_define_rooms (request,name):
    date = datetime.datetime.now()
    gardesh = Gardesh.objects.get(name = name)
    hotel = Hotel.objects.get(gardesh = gardesh)
    position = 'ارائه اتاق های هتل'
    username = ''
    builder = ''
    u1 = request.user
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)

    if request.POST.get("save","")!= "":
        form = HotelRoomForm(request.POST)
        if form.is_valid():
            print('valid')
            num = request.POST.get('number')
            ran = range(1,int(num))
            for i in ran :
                if request.POST.get('s'+str(i))!="" and request.POST.get('e'+str(i))!="" and request.POST.get('p'+str(i))!="" and request.POST.get('c'+str(i))!="":
                    start = request.POST.get('s'+str(i))
                    end = request.POST.get('e'+str(i))
                    day_start = form.cleaned_data['start']
                    day_end = form.cleaned_data['end']
                    print(str(i)+'s')
                    ran2 = range(int(start),int(end)+1)
                    print(str(i)+'p')
                    for j in ran2:
                        for single_date in daterange(day_start, day_end):
                            # print(single_date.strftime("%Y-%m-%d"))

                            room = Room()
                            room.hotel = hotel
                            room.capacity = int(request.POST.get('c'+str(i)))
                            room.cost_perNight = int(request.POST.get('p'+str(i)))
                            room.number = j
                            room.date = single_date
                            room.save()
            return HttpResponseRedirect('/userpage/')

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = HotelRoomForm()

    return render(request, "hotel_define_rooms.html",{
        'gardesh': gardesh,
        'hotel': hotel,
        'username': username,
        'form': form,
        'b': builder,
        'user2':u1,
        'position':position,
        'tarikh':date,
    })

@login_required()
def hotel_define_2(request,id):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'تعریف یک هتل> تایید اطلاعات'
    gardesh = Gardesh.objects.get(id = id)
    hotel = Hotel.objects.get(gardesh = gardesh)
    if request.POST.get("return","") != "":
        hotel.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/hotel/')
    if request.POST.get("cancel","") != "":
        hotel.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/tourdefine/hotel/rooms/'+str(gardesh.name))

    return render(request, "hotel_define_2.html",{
        'gardesh': gardesh,
        'hotel': hotel,
        'username':"gardeshsaz",
        'user2':user2,
        'position':position,
        'tarikh':date,
    })

@login_required()
def restaurant_define(request):
    date = datetime.datetime.now()
    username = ''
    builder = ''
    u1 = request.user
    position = 'تعریف یک رستوران'
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)

    if request.POST.get("save","") != "":
        form = RestaurantForm(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = form.cleaned_data['name']
            gardesh.builder = builder
            gardesh.kind = 'restaurant'
            a = Agreement()
            a.kind ='r-g'
            a.percent = '7'
            a.save()
            gardesh.agreement = a
            gardesh.degree = 'G'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if request.POST.get('other_explain'):
                gardesh.other_explain = request.POST.get('other_explain')
                print(gardesh.other_explain)
            gardesh.save()
            f.gardesh = gardesh
            if form.cleaned_data['pic1']:
                pic1 = Picture()
                pic1.picture = form.cleaned_data['pic1']
                pic1.gardesh = gardesh
                pic1.save()
            if form.cleaned_data['pic2']:
                pic2 = Picture()
                pic2.picture = form.cleaned_data['pic2']
                pic2.gardesh = gardesh
                pic2.save()
            if form.cleaned_data['pic3']:
                pic3 = Picture()
                pic3.picture = form.cleaned_data['pic3']
                pic3.gardesh = gardesh
                pic3.save()
            if form.cleaned_data['pic4']:
                pic4 = Picture()
                pic4.picture = form.cleaned_data['pic4']
                pic4.gardesh = gardesh
                pic4.save()
            if request.POST.get('address'):
                f.address = request.POST.get('address')
            f.save()
            return HttpResponseRedirect('/tourdefine/restaurant/2/'+str(gardesh.id))

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = RestaurantForm()

    return render(request,"restaurant_define.html",{
        'username': username,
        'form': form,
        'b': builder,
        'user2':u1,
        'position':position,
        'tarikh':date,
    })

@login_required()
def restaurant_define_rooms (request,name):
    date = datetime.datetime.now()
    gardesh = Gardesh.objects.get(name = name)
    res = Restaurant.objects.get(gardesh = gardesh)
    username = ''
    builder = ''
    position = 'ارائه میزهای رستوران'
    u1 = request.user
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)

    if request.POST.get("save","")!= "":
        form = RestaurantRoomForm(request.POST)
        if form.is_valid():
            print('valid')
            num = request.POST.get('number')
            ran = range(1,int(num))
            for i in ran :
                if request.POST.get('n'+str(i))!="" and request.POST.get('s'+str(i))!="" and request.POST.get('e'+str(i))!="" and request.POST.get('p'+str(i))!="" and request.POST.get('c'+str(i))!="":
                    start = request.POST.get('s'+str(i))
                    end = request.POST.get('e'+str(i))
                    numbert = request.POST.get('n'+str(i))
                    day_start = form.cleaned_data['start']
                    day_end = form.cleaned_data['end']
                    print(str(i)+'s')
                    ran2 = range(int(start),int(end)+1)
                    print(str(i)+'p')
                    for j in ran2:
                        for single_date in daterange(day_start, day_end):
                            # print(single_date.strftime("%Y-%m-%d"))
                            table = Table()
                            table.restaurant = res
                            table.capacity = int(request.POST.get('c'+str(i)))
                            table.cost_perClock = int(request.POST.get('p'+str(i)))
                            table.number = int(numbert)
                            table.date = single_date
                            table.start_clock = str(j)+':00'
                            table.save()
            return HttpResponseRedirect('/userpage/')

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = RestaurantRoomForm()

    return render(request, "restaurant_define_tables.html",{
        'gardesh': gardesh,
        'res': res,
        'username': username,
        'form': form,
        'b': builder,
        'user2':u1,
        'position':position,
        'tarikh':date,
    })

@login_required()
def restaurant_define_2(request,id):
    date = datetime.datetime.now()
    position = 'تعریف یک رستوران> تایید اطلاعات'
    user2 = request.user
    gardesh = Gardesh.objects.get(id = id)
    restaurant = Restaurant.objects.get(gardesh = gardesh)
    if request.POST.get("return","") != "":
        restaurant.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/restaurant/')
    if request.POST.get("cancel","") != "":
        restaurant.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/tourdefine/restaurant/tables/'+str(gardesh.name))

    return render(request, "restaurant_define_2.html",{
        'gardesh': gardesh,
        'restaurant': restaurant,
        'username':"gardeshsaz",
        'user2':user2,
        'position':position,
        'tarikh':date,
    })

@login_required()
def cancel(request,name):
    date = datetime.datetime.now()
    return render(request,"cancel.html",{
        'username': 'gardeshsaz',
        'tarikh':date,
    })

@login_required()
def restaurant_define_first(request):
    date = datetime.datetime.now()
    u1 = request.user
    position = 'لیست رستوران ها'
    username = ''
    builder = ''
    names = []
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)
                gardeshs = Gardesh.objects.filter(builder = builder)
                for g in gardeshs:
                    names += [g.name]

    if request.POST.get("define","") != "":
        return HttpResponseRedirect('/tourdefine/restaurant/define/')

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')

    return render(request,"restaurant_define_1.html",{
        'username': username,
        'b': builder,
        'user2': u1,
        'position': position,
        'names': names,
        'tarikh':date,
    })
