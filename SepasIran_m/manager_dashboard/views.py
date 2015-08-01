from django.shortcuts import render
from quality_control.models import OnlineComment
# Create your views here.

def Dashboard(request):
    onlineComments = OnlineComment.objects.all()
    return render(request, "manager_dashboard.html", {"onlineComments": onlineComments})


def tourLists(request):
    return render(request, "manager_tours.html", {"username": "admin"})


def tourRating(request):
    return render(request, "manager_tours_rating.html", {"username": "admin"})


def showOnlineComments(request):
    onlineComments = OnlineComment.objects.all()
    return render(request, "manager_online_comments.html", {"onlineComments": onlineComments})


def userLists(request):
    return render(request, "manager_gardeshgar_info.html", {"username": "admin"})



def paymentLists(request):
    return render(request, "manager_paymentList.html", {"username": "admin"})

def contractPercent(request):
    return render(request, "manager_contract_percent.html", {"username": "admin"})