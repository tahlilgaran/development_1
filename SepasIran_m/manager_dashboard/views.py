import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounting.models import Trans_info
from define_trip.models import Tour, Picture
from quality_control.models import OnlineComment
# Create your views here.
from user.models import TouristProfile, TourBuilderProfile, UserM


def Dashboard(request):
    onlineComments = OnlineComment.objects.all()[0:5]
    tours = Tour.objects.filter(end__gt=datetime.datetime.today(),
                                start__lt=datetime.date.today())[0:3]
    return render(request, "manager_dashboard.html", {"onlineComments": onlineComments , "runningTours" : tours})


def tourLists(request):
    tours = Tour.objects.filter(end__gt=datetime.datetime.today(),
                            start__lt=datetime.date.today())
    tour =tours[0]
    print(tour.gardesh.builder.user.picture)
    pics =[]
    for tour in tours :
        pic = Picture.objects.filter(gardesh = tour.gardesh)
        if not pic :
            pics.append(tour.gardesh.builder.user.picture)
        else :
            pics.append(pic)

    return render(request, "manager_tours.html", {"runningTours": tours , "pics" : pics  })


def tourRating(request):
    gold_tours = Tour.objects.filter(gardesh__degree = "G")
    silver_tours = Tour.objects.filter(gardesh__degree = "S")
    bronze_tours = Tour.objects.filter(gardesh__degree = "B")

    return render(request, "manager_tours_rating.html", {"gold_tours": gold_tours ,"silver_tours": silver_tours ,"bronze_tours": bronze_tours })


def showOnlineComments(request):
    onlineComments = OnlineComment.objects.all()
    return render(request, "manager_online_comments.html", {"onlineComments": onlineComments})


def showTouristList(request):
    List = TouristProfile.objects.all()
    return render(request, "manager_gardeshgar_info.html", {"header":"گردشگران" ,"list": List})

def showTourBuilderList(request):
    List = TourBuilderProfile.objects.all()
    return render(request, "manager_gardeshgar_info.html", {"header": "گردش سازان", "list": List})


def touristSearch(request):
    user=User.objects.filter(username__contains = request.GET.get("username"))
    print(user)
    userM = UserM.objects.filter(user = user)
    List = TouristProfile.objects.filter(user = userM)
    print(List)
    return render(request, "manager_gardeshgar_info.html", {"header":"گردشگران" ,"list": List})

def tourBuilderSearch(request):
    user=User.objects.filter(username__contains = request.GET.get("username"))
    print(user)
    userM = UserM.objects.filter(user = user)
    List = TourBuilderProfile.objects.filter(user = userM)
    return render(request, "manager_gardeshgar_info.html", {"header": "گردش سازان", "list": List})



def paymentLists(request):
    transList = Trans_info.objects.all()

    return render(request, "manager_paymentList.html", {"transList": transList})

def contractPercent(request):
    return render(request, "manager_contract_percent.html", {"username": "admin"})


def saveContractPercent(request):
    return redirect("/manager/Dashboard/")