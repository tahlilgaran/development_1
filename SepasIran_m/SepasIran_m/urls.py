
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

    # present trip urls :
    url(r'home/$', 'present_trip.views.home'),
    url(r'home/(\w+)/$', 'present_trip.views.home'),
    url(r'show/(\w+)/(\d+)/$' , 'present_trip.views.show_one_trip'),
    url(r'show/(\w+)/(\d+)/status/$', 'present_trip.views.show_one_trip_status'),
    url(r'show/(\w+)/(\d+)/(\d+)/status/$', 'present_trip.views.show_one_trip_status'),
    # url(r'show/(\w+)/$', 'present_trip.views.show_one_trip'),
    # url(r'show/(\w+)/(\w+)$', 'present_trip.views.show_one_trip'),
    # url(r'show/(\w+)/(\w+)/status/$', 'present_trip.views.show_one_trip_status'),
    # url(r'search/$', 'present_trip.views.start_search'),
    url(r'search/$', 'present_trip.views.search'),
    # url(r'search/result/$', 'present_trip.views.search'),
    # url(r'search/result/(\w+)/$', 'present_trip.views.search'),
    # url(r'search/result/(\w+)/(\w+)$', 'present_trip.views.search'),

    #informing urls:
    # url(r'userpage/$', 'informing.views.account'),
    url(r'userpage/$', 'informing.views.account'),



    # url(r'help/$', 'informing.views.help'),
    url(r'cancelselling/(\w+)$','define_trip.views.cancel'),
    url(r'tourdefine/$', 'define_trip.views.tarif_kind'),
    url(r'tourdefine/(\w+)$', 'define_trip.views.tarif_kind'),
    url(r'tourdefine/tour/$','define_trip.views.tour_define'),
    url(r'tourdefine/tour/(\w+)$','define_trip.views.tour_define'),
    url(r'tourdefine/tour/2/(\d+)$','define_trip.views.tour_define_2'),
    url(r'tourdefine/tour/change/(\w+)$','define_trip.views.tour_define'),
    url(r'tourdefine/airplane/$','define_trip.views.airplane_define'),
    url(r'tourdefine/airplane/2/(\d+)$','define_trip.views.airplane_define_2'),
    url(r'tourdefine/train/$','define_trip.views.train_define'),
    url(r'tourdefine/train/2/(\d+)/$','define_trip.views.train_define_2'),
    url(r'tourdefine/hotel/$','define_trip.views.hotel_define'),
    url(r'tourdefine/hotel/2/(\d+)/$','define_trip.views.hotel_define_2'),
    url(r'tourdefine/restaurant/$','define_trip.views.restaurant_define'),
    url(r'tourdefine/restaurant/2/(\d+)/$','define_trip.views.restaurant_define_2'),
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

   url(r'reserving/restaurant/<(P?<id>\d+)/$', 'buy_cancel.views.reserveResturant'),
    url(r'reserving/restaurant/(\d+)/$', 'buy_cancel.views.reserveResturant'),

   url(r'reserving/hotel/<(P?<room_id>\d+)/>/$', 'buy_cancel.views.reserveHotel'),
       url(r'reserving/hotel/(\d+)/$', 'buy_cancel.views.reserveHotel'),

   url(r'reserving/tour/<(P?<tour_id>\d+)>/$', 'buy_cancel.views.reserveTour'),
     url(r'reserving/tour/(\d+)/$', 'buy_cancel.views.reserveTour'),
     url(r'reserving/tour/(\d+)/number/$', 'buy_cancel.views.reserveTour'),

   url(r'reserving/airplane/<(P?<id>\d+)>/$', 'buy_cancel.views.reserveAirplane'),
    url(r'reserving/airplane/(\d+)/$', 'buy_cancel.views.reserveAirplane'),

   url(r'reserving/train/<(P?<id>\d+)>/$', 'buy_cancel.views.reserveTrain'),
    url(r'reserving/train/(\d+)/$', 'buy_cancel.views.reserveTrain'),
  # url(r'reserving/status/(<P?<kind>\w+>)/(<P?<id>\d+>)/$', 'buy_cancel.views.statusReserve'),

     url(r'reserving/status/(\w+)/(\d+)/$', 'buy_cancel.views.statusReserve'),


   url(r'purchase/restaurant/<(P?<id>\d+)/<(p?<capacity>\d+)>/$', 'buy_cancel.views.purchaseResturant'),
     url(r'purchase/restaurant/(\d+)/$', 'buy_cancel.views.purchaseResturant'),
      url(r'payment/restaurant/(\d+)/$', 'accounting.views.paymentRestaurant'),
       url(r'payment/restaurant/confirm/(\d+)/$', 'accounting.views.confirmRestaurant'),

   url(r'purchase/hotel/<(P?<room_id>\d+)/>/$', 'buy_cancel.views.purchaseHotel'),
    url(r'purchase/hotel/(\d+)/$', 'buy_cancel.views.purchaseHotel'),
     url(r'payment/hotel/(\d+)/$', 'accounting.views.paymentHotel'),
      url(r'payment/hotel/confirm/(\d+)/$', 'accounting.views.confirmHotel'),


   url(r'purchase/airplane/(\d+)/$', 'buy_cancel.views.purchaseAirplane'),
    url(r'payment/airplane/(\d+)/$', 'accounting.views.paymentAirplane'),
     url(r'payment/airplane/confirm/(\d+)/$', 'accounting.views.confirmAirplane'),

   url(r'purchase/train/<(P?<id>\d+)>/$', 'buy_cancel.views.purchaseTrain'),
    url(r'purchase/train/(\d+)/$', 'buy_cancel.views.purchaseTrain'),
     url(r'payment/train/(\d+)/$', 'accounting.views.paymentTrain'),
      url(r'payment/train/confirm/(\d+)/$', 'accounting.views.confirmTrain'),

   #url(r'purchase/(<P?<kind>\w+>)/confirm$', 'buy_cancel.views.confirmPurchase'),
     url(r'purchase/tour/(\d+)/$', 'buy_cancel.views.purchaseTour'),
      url(r'payment/tour/(\d+)/$', 'accounting.views.paymentTour'),
       url(r'payment/tour/confirm/(\d+)/$', 'accounting.views.confirmTour'),

     url(r'payment/$', 'accounting.views.ozviyat'),

   # url(r'payment/confirm/$', 'accounting.views.confirm'),
   url(r'^manager/', include('manager_dashboard.urls')),
   url(r'^quality/', include('quality_control.urls')),
   url(r'^admin/', include(admin.site.urls)),
]
