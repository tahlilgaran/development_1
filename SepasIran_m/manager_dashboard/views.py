import datetime
from django.shortcuts import render
from accounting.models import Trans_info
from define_trip.models import Tour
from quality_control.models import OnlineComment
# Create your views here.
from user.models import TouristProfile, TourBuilderProfile


def Dashboard(request):
    onlineComments = OnlineComment.objects.all()[0:5]
    tours = Tour.objects.filter(end__gt=datetime.datetime.today(),
                                start__lt=datetime.date.today())[0:3]
    return render(request, "manager_dashboard.html", {"onlineComments": onlineComments , "runningTours" : tours})


def tourLists(request):
    tours = Tour.objects.filter(end__gt=datetime.datetime.today(),
                                start__lt=datetime.date.today())

    return render(request, "manager_tours.html", {"runningTours": tours})


def tourRating(request):
    return render(request, "manager_tours_rating.html", {"username": "admin"})


def showOnlineComments(request):
    onlineComments = OnlineComment.objects.all()
    return render(request, "manager_online_comments.html", {"onlineComments": onlineComments})


def showTouristList(request):
    List = TouristProfile.objects.all()
    return render(request, "manager_gardeshgar_info.html", {"header":"گردشگران" ,"list": List})

def showTourBuilderList(request):
    List = TourBuilderProfile.objects.all()
    return render(request, "manager_gardeshgar_info.html", {"header": "گردش سازان", "list": List})



def paymentLists(request):
    transList = Trans_info.objects.all()

    return render(request, "manager_paymentList.html", {"transList": transList})

def contractPercent(request):
    return render(request, "manager_contract_percent.html", {"username": "admin"})