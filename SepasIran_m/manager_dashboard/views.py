import datetime
from django.contrib.auth.models import User
from django.shortcuts import render
from accounting.models import Trans_info
from buy_cancel.models import Wanted_Tour
from define_trip.models import Tour, Picture, Agreement
from manager_dashboard.templatetags.miladitoshamsi import miladitoshamsi
from quality_control.models import OnlineComment, RatingComment
# Create your views here.
from user.models import TouristProfile, TourBuilderProfile, UserM


def Dashboard(request):
    onlineComments = OnlineComment.objects.all()[0:5]
    tours = Tour.objects.filter(end__gt=datetime.datetime.today(),
                                start__lt=datetime.date.today())[0:3]
    #todo momkene month-3 manfi beshe :D
    date_3_month_ago = datetime.date(day=1, month=datetime.date.today().month - 3, year=datetime.date.today().year)

    users_rating = []
    comments = RatingComment.objects.filter(date__gt=date_3_month_ago)
    users_rating.append(0)
    users_rating.append(0)
    users_rating.append(0)
    users_rating.append(0)
    users_rating.append(0)
    for comment in comments:
        users_rating[0] = users_rating[0] + comment.Q1
        users_rating[1] = users_rating[1] + comment.Q2
        users_rating[2] = users_rating[2] + comment.Q3
        users_rating[3] = users_rating[3] + comment.Q4
        users_rating[4] = users_rating[4] + comment.Q5

    users_rating[0] = (6 * len(comments)) - users_rating[0]
    users_rating[1] = (6 * len(comments)) - users_rating[1]
    users_rating[2] = (6 * len(comments)) - users_rating[2]
    users_rating[3] = (6 * len(comments)) - users_rating[3]
    users_rating[4] = (6 * len(comments)) - users_rating[4]

    #todo momkene day-10 manfi beshe :D
    #date_10_day_ago = datetime.date(day=datetime.date.today().day-10, month=datetime.date.today().month, year=datetime.date.today().year)
    finished_tours = Tour.objects.filter(end__lt=datetime.date.today())
    rating_comments = RatingComment.objects.filter(tour=finished_tours)
    tour_contributer = Wanted_Tour.objects.filter(gardesh=finished_tours)
    contributing=[]
    contributing.append(len(rating_comments))
    contributing.append(len(tour_contributer)-len(rating_comments))
    print(len(tour_contributer))
    print(len(rating_comments))



    return render(request, "manager_dashboard.html",
                  {"onlineComments": onlineComments, "runningTours": tours, 'user_rating': users_rating , 'contributing': contributing})


def tourLists(request):
    tours = Tour.objects.filter(end__gt=datetime.datetime.today(),
                                start__lt=datetime.date.today())
    pics = []
    for tour in tours:
        pic = Picture.objects.filter(gardesh=tour.gardesh)
        if not pic:
            pics.append(tour.gardesh.builder.user.picture)
        else:
            pics.append(pic)

    return render(request, "manager_tours.html", {"runningTours": tours, "pics": pics})


def tourRating(request):
    gold_tours = Tour.objects.filter(gardesh__degree="G")
    silver_tours = Tour.objects.filter(gardesh__degree="S")
    bronze_tours = Tour.objects.filter(gardesh__degree="B")

    return render(request, "manager_tours_rating.html",
                  {"gold_tours": gold_tours, "silver_tours": silver_tours, "bronze_tours": bronze_tours})


def showOnlineComments(request):
    onlineComments = OnlineComment.objects.all()
    users=[]
    for c in onlineComments:
        if not c.user in users:
            users.append(c.user)

    toursb = Wanted_Tour.objects.filter(gardesh=Tour.objects.filter(start__lt=datetime.date.today()))

    comment_st = []
    comment_st.append(len(users))
    comment_st.append(len(toursb)-len(users))

    return render(request, "manager_online_comments.html", {"onlineComments": onlineComments , 'comment_st' : comment_st})


def showTouristList(request):
    List = TouristProfile.objects.all()
    return render(request, "manager_gardeshgar_info.html", {"header": "گردشگران", "list": List})


def showTourBuilderList(request):
    List = TourBuilderProfile.objects.all()
    return render(request, "manager_gardeshgar_info.html", {"header": "گردش سازان", "list": List})


def touristSearch(request):
    print("search")
    user = User.objects.filter(username__contains=request.GET.get("username"))
    print(user)
    userM = UserM.objects.filter(user=user)
    List = TouristProfile.objects.filter(user=userM)
    print(List)
    return render(request, "manager_gardeshgar_info.html", {"header": "گردشگران", "list": List})


def tourBuilderSearch(request):
    user = User.objects.filter(username__contains=request.GET.get("username"))
    print(user)
    userM = UserM.objects.filter(user=user)
    List = TourBuilderProfile.objects.filter(user=userM)
    return render(request, "manager_gardeshgar_info.html", {"header": "گردش سازان", "list": List})


def paymentLists(request):
    transList = Trans_info.objects.all()

    return render(request, "manager_paymentList.html", {"transList": transList})


def contractPercent(request):
    try:
        percent = Agreement.objects.all()[0].percent
    except:
        percent = 0
    last_agreements = Agreement.objects.all()
    if len(last_agreements) > 5:
        last_agreements = [last_agreements[len(last_agreements) - 6], last_agreements[len(last_agreements) - 5],
                           last_agreements[len(last_agreements) - 4], last_agreements[len(last_agreements) - 3],
                           last_agreements[len(last_agreements) - 2], last_agreements[len(last_agreements) - 1]]

    dates = []
    percents = []
    for ag in last_agreements:
        dates.append(miladitoshamsi(ag.date))
        percents.append(ag.percent)

    dates = reversed(dates)

    a = ["اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد"]
    return render(request, "manager_contract_percent.html",
                  {"new_percent": percent, 'dates': dates, 'percents': percents})


def saveContractPercent(request):
    if (int(request.GET.get("percent")) < 100 ):
        agreement = Agreement()
        agreement.kind = "tour"
        agreement.percent = request.GET.get("percent")
        agreement.save()

    return contractPercent(request)
