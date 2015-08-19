__author__ = 'M'
# -*- coding: utf-8 -*-


from django.conf.urls import url

urlpatterns = [
    url(r'onlineComment/(\d+)$', 'quality_control.views.show_online_comment_form'),
    url(r'saveOnlineComment/(\d+)$', 'quality_control.views.online_comment'),
    url(r'userRating/(\d+)$', 'quality_control.views.show_user_rating_form'),
     url(r'saveUserRating/(\d+)$', 'quality_control.views.user_rating'),
]