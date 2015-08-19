import datetime
from django.shortcuts import render, redirect

# Create your views here.
from define_trip.models import Tour
from quality_control.models import OnlineComment, RatingComment


def user_rating(request , tour_id):
    if (request.method == 'POST'):
        #user = UserM.objects.filter(user= request.user)
        new_comment = RatingComment()
        new_comment.Q1 = request.POST.get('Q1')
        new_comment.Q2 = request.POST.get('Q2')
        new_comment.Q3 = request.POST.get('Q3')
        new_comment.Q4 = request.POST.get('Q4')
        new_comment.Q5 = request.POST.get('Q5')
        new_comment.user = request.user.userm
        tour = Tour.objects.get(id=tour_id)
        new_comment.tour = tour
        new_comment.date = datetime.datetime.now()
        new_comment.save()

    return redirect("/userpage/")  #todo RENDER SUCCESS MSG  /userpage/gardeshgar


def show_user_rating_form(request , tour_id):
    return render(request, "quality_user_rating.html",
                  {'user2': request.user, 'position': "سامانه کنترل کیفت - نظرسنجی پایان تور",
                   'tarikh': datetime.datetime.now(), 'tour_id' : tour_id})


def online_comment(request , tour_id):  #todo bayad tour_id ro ham begiram tu url
    if (request.method == 'POST'):
        #f = OnlineCommentForm(request.POST)
        new_comment = OnlineComment()
        new_comment.body = request.POST.get('body')
        new_comment.user = request.user.userm
        tour = Tour.objects.get(id=tour_id)
        new_comment.tour = tour
        new_comment.date = datetime.datetime.now()
        new_comment.save()

    return redirect("/userpage/")


def show_online_comment_form(request , tour_id):
    tour = Tour.objects.filter(id= tour_id)
    return render(request, "quality_online_comment.html",
                  {'user2': request.user, 'position': "سامانه کنترل کیفیت - نظرسنجی برخط",
                   'tarikh': datetime.datetime.now() , "tour_id" : tour_id
                  })

