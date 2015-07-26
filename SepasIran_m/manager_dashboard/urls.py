__author__ = 'M'
# -*- coding: utf-8 -*-


from django.conf.urls import url

urlpatterns = [
    url(r'Dashboard/$', 'manager_dashboard.views.Dashboard'),
    url(r'tourLists/$', 'manager_dashboard.views.tourLists'),
    url(r'tourRating/$', 'manager_dashboard.views.tourRating'),
    url(r'userLists/$', 'manager_dashboard.views.userLists'),
    url(r'paymentsList/$', 'manager_dashboard.views.paymentLists'),
    url(r'contractPercent/$', 'manager_dashboard.views.contractPercent'),
    url(r'OnlineComments/$', 'manager_dashboard.views.showOnlineComments'),
]