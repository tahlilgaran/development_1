import datetime
from django.shortcuts import render

# Create your views here.
from quality_control.models import  OnlineCommentForm, OnlineComment


def user_rating(request, tour_id):
    pass
    #if (request.method == 'POST'):
    #    f = RatingCommentForm(request.POST)
    #    new_comment = f.save()
    #    new_comment.user = request.user
    #    #tour = Tour.objects.get(id=tour_id)  #todo
    #    #new_comment.tour = tour   #todo
    #    new_comment.date = datetime.datetime.now()
    #    new_comment.save()
    #return render(request, "quality_user_rating.html", {"username": "gardeshgar"})   #todo RENDER SUCCESS MSG


def show_user_rating_form(request):
    return render(request, "quality_user_rating.html", {"username": "gardeshgar"})


def online_comment(request):  #todo bayad tour_id ro ham begiram tu url
    if (request.method == 'POST'):
        #f = OnlineCommentForm(request.POST)
        new_comment = OnlineComment()
        new_comment.body = request.POST.get('body')
        new_comment.user = request.user
        #tour = Tour.objects.get(id=tour_id)  #todo
        #new_comment.tour = tour   #todo
        new_comment.date = datetime.datetime.now()
        new_comment.save()

    return render(request, "quality_online_comment.html", {"username": "gardeshgar"})  #todo RENDER SUCCESS MSG  /userpage/gardeshgar


def show_online_comment_form(request):
    return render(request, "quality_online_comment.html", {"username": "gardeshgar"})

