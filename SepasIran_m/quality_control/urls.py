__author__ = 'M'
# -*- coding: utf-8 -*-


from django.conf.urls import url

urlpatterns = [
    url(r'onlineComment/$', 'quality_control.views.show_online_comment_form'),
    url(r'saveOnlineComment/$', 'quality_control.views.online_comment'),
    url(r'userRating/$', 'quality_control.views.user_rating'),
]