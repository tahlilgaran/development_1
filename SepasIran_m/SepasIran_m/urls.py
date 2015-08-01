
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

    # present trip urls :
    url(r'home/$', 'present_trip.views.home'),
    url(r'home/(\w+)/$', 'present_trip.views.home'),
    url(r'show/(\w+)/(\d+)/$' , 'present_trip.views.show_one_trip'),
    url(r'show/(\w+)/(\d+)/status/$', 'present_trip.views.show_one_trip_status'),
    # url(r'show/(\w+)/$', 'present_trip.views.show_one_trip'),
    # url(r'show/(\w+)/(\w+)$', 'present_trip.views.show_one_trip'),
    # url(r'show/(\w+)/(\w+)/status/$', 'present_trip.views.show_one_trip_status'),
    url(r'search/form/$', 'present_trip.views.start_search'),
    url(r'search/form/(\w+)/$', 'present_trip.views.start_search'),
    url(r'search/result/$', 'present_trip.views.search'),
    url(r'search/result/(\w+)/$', 'present_trip.views.search'),
    url(r'search/result/(\w+)/(\w+)$', 'present_trip.views.search'),

    #informing urls:
    # url(r'userpage/$', 'informing.views.account'),
    url(r'userpage/\w+/$', 'informing.views.account'),



    # url(r'help/$', 'informing.views.help'),
    url(r'cancelselling/(\w+)$','define_trip.views.cancel'),
    url(r'tourdefine/$', 'define_trip.views.tarif_kind'),
    url(r'tourdefine/(\w+)$', 'define_trip.views.tarif_kind'),
    url(r'tourdefine/tour/$','define_trip.views.tour_define'),
    url(r'tourdefine/tour/(\w+)$','define_trip.views.tour_define'),
    url(r'tourdefine/tour/change/(\w+)$','define_trip.views.tour_define'),
    url(r'tourdefine/airPlane/(\w+)$','define_trip.views.airplane_define'),
    url(r'tourdefine/train/(\w+)/$','define_trip.views.train_define'),
    url(r'signup/$', 'user.views.signup'),
    url(r'signIn/$', 'user.views.signin'),
    url(r'logout/$', 'user.views.logout_view'),
    url(r'forgetpassword/$', 'user.views.forget_password'),
    url(r'signup/tourist/$', 'user.views.tourist_signup'),
    url(r'signup/tourist/2/(\w+)/$', 'user.views.tourist_signup_2'),
    url(r'signup/tourBuilder/(\w+)$', 'user.views.servant_signup'),
    url(r'signup/tourBuilder/$', 'user.views.servant_signup'),
    url(r'signup/tourBuilder/2/(\d+)/(\d+)$', 'user.views.servant_signup_2'),
    url(r'edit/tourist/(\w+)$','user.views.edit_tourist'),
    url(r'profile/tourist/(\w+)$','user.views.tourist_profile'),
    url(r'profile/tourbuilder/(\w+)$','user.views.tourbuilder_profile'),
    url(r'edit/tourbuilder/(\w+)$','user.views.edit_tourbuilder'),

   # url(r'reserve/(P?<tour_id>\d+)/$', 'buy_cancel.views.reserve'),

   url(r'reserving/resturant/<(P?<id>\d+)/<(p?<capacity>\d+)>/$', 'buy_cancel.views.reserveResturant'),
   url(r'reserving/hotel/<(P?<room_id>\d+)/>/$', 'buy_cancel.views.reserveHotel'),
   url(r'reserving/tour/<(P?<tour_id>\d+)>/$', 'buy_cancel.views.reserveTour'),
   url(r'reserving/airplane/<(P?<id>\d+)>/$', 'buy_cancel.views.reserveAirplane'),
   url(r'reserving/train/<(P?<id>\d+)>/$', 'buy_cancel.views.reserveTrain'),
   url(r'reserveing/(<P?<kind>\w+>)/confirm$', 'buy_cancel.views.confirmReserve'),

   url(r'purchase/resturant/<(P?<id>\d+)/<(p?<capacity>\d+)>/$', 'buy_cancel.views.purchaseResturant'),
   url(r'purchase/hotel/<(P?<room_id>\d+)/>/$', 'buy_cancel.views.purchaseHotel'),
   url(r'purchase/tour/<(P?<tour_id>\d+)>/$', 'buy_cancel.views.purchaseTour'),
   url(r'purchase/airplane/<(P?<id>\d+)>/$', 'buy_cancel.views.purchaseAirplane'),
   url(r'purchase/train/<(P?<id>\d+)>/$', 'buy_cancel.views.purchaseTrain'),
   #url(r'purchase/(<P?<kind>\w+>)/confirm$', 'buy_cancel.views.confirmPurchase'),

   #  url(r'reserve/([service][tour])/$', 'buy_cancel.views.reserve'),
  # url(r'purchase/(P?<tour_id>\d+)/$', 'buy_cancel.views.purchase'),
  # url(r'purchase/(\w+)/$', 'buy_cancel.views.purchase'),
  # url(r'purchase/$', 'buy_cancel.views.purchase'),
 #  url(r'purchase/(P?<tour_id>\d+)/$', 'buy_cancel.views.purchase'),
 #   url(r'cancel/(\w+)/$', 'accounting.views.cancel'),
   url(r'payment/(P?<tour_id>\d+)/(p?<number>\d+)/$', 'accounting.views.paymentTour'),
   # url(r'payment/Confirm/(P?<id>\d+)/$', 'accounting.views.confirm'),
   # url(r'payment/$', 'accounting.views.payment'),
   url(r'payment/confirm/(P?<tour_id>\d+)/$', 'accounting.views.confirmTour'),
   # url(r'payment/confirm/$', 'accounting.views.confirm'),
   url(r'^manager/', include('manager_dashboard.urls')),
   # url(r'^quality/', include('quality_control.urls')),
   url(r'^admin/', include(admin.site.urls)),
]
