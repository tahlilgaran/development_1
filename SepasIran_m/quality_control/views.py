import datetime
from django.shortcuts import render, redirect

# Create your views here.
from define_trip.models import Tour
from quality_control.models import  OnlineCommentForm, OnlineComment , RatingComment


def user_rating(request):
        #f = RatingCommentForm(request.POST)
        #new_comment = f.save()
        #new_comment.user = request.user
        ##tour = Tour.objects.get(id=tour_id)  #todo
        ##new_comment.tour = tour   #todo
        #new_comment.date = datetime.datetime.now()
        #new_comment.save()

    if (request.method == 'POST'):
        #f = OnlineCommentForm(request.POST)
        new_comment = RatingComment()
        new_comment.Q1 = request.POST.get('Q1')
        new_comment.Q2 = request.POST.get('Q2')
        new_comment.Q3 = request.POST.get('Q3')
        new_comment.Q4 = request.POST.get('Q4')
        new_comment.Q5 = request.POST.get('Q5')
        new_comment.user = request.user
        #tour = Tour.objects.get(id=tour_id)  #todo
        #new_comment.tour = tour   #todo
        new_comment.date = datetime.datetime.now()
        new_comment.save()

    return render(request, "quality_online_comment.html", {"username": "gardeshgar"})  #todo RENDER SUCCESS MSG  /userpage/gardeshgar


    return render(request, "quality_user_rating.html", {"username": "gardeshgar"})   #todo RENDER SUCCESS MSG


def show_user_rating_form(request):
    return render(request, "quality_user_rating.html", {"username": "gardeshgar"})


def online_comment(request):  #todo bayad tour_id ro ham begiram tu url
    if (request.method == 'POST'):
        #f = OnlineCommentForm(request.POST)
        new_comment = OnlineComment()
        new_comment.body = request.POST.get('body')
        new_comment.user = request.user.userm
        tour = Tour.objects.get(id=2)  #todo
        new_comment.tour = tour   #todo
        new_comment.date = datetime.datetime.now()
        new_comment.save()

    return redirect("/userpage/")


def show_online_comment_form(request):
    return render(request, "quality_online_comment.html", {"username": "gardeshgar"})

