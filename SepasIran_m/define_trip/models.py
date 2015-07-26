from django.db import models
import datetime
from user.models import TourBuilderProfile


class Agreement(models.Model):
    percent = models.FloatField()    # between 0 and 1
    kind = models.CharField()   # tr-b /tr-s /tr-g/ a-b /...


class Gardesh(models.Model):
    builder = models.ForeignKey(TourBuilderProfile)
    kind = models.CharField()   # t/tr/a/h/r
    final_rank = models.FloatField(null=True,blank=True)
    order_rank = models.FloatField(null=True,blank=True)
    comment_rank = models.FloatField(null=True,blank=True)
    degree = models.CharField()     # g/s/b
    max_cancel_time = models.IntegerField(default= 2)
    free = models.FloatField(default=1)     # between 0 and 1
    define_time = models.DateTimeField(default= datetime.datetime.now)
    agreement = models.ForeignKey(Agreement)


class Tour(models.Model):
    name = models.CharField(max_length=255)
    gardesh = models.ForeignKey(Gardesh, related_name='tour')
    tour_kind = models.CharField()      # nat / inter / holly
    destination = models.CharField()    # city name
    source = models.CharField()         # city name
    start = models.DateField()
    start_t = models.TimeField()
    end = models.DateField()
    end_t = models.TimeField()
    capacity = models.IntegerField()    # tedadi ke mitavanim befrooshim
    has_sold = models.IntegerField(default=0)   # if = capacity or intire=0 => stop selling
    entire_capacity = models.IntegerField()     # mizani ke hanooz az zarfiate kol mande
    leader = models.CharField()
    leader_c = models.CharField(null=True, blank=True)
    transfer_device = models.ForeignKey(TransferDevice)
    stay_location = models.ForeignKey(Location)
    exclusive_cost = models.IntegerField()  # with out bazdid
    entire_cost = models.IntegerField()
    destination_explain = models.TextField(null=True, blank=True)
    move_explain = models.TextField(null=True, blank=True)
    other_explain = models.TextField(null=True, blank=True)


class TransferDevice(models.Model):
    kind = models.CharField(max_length=1)    # a/t/b
    degree = models.CharField(max_length=2)      # g/s/b
    name = models.CharField(max_length=255)


class Location(models.Model):
    kind = models.CharField(max_length=1)    # h/a/m
    degree = models.CharField(max_length=2)      # g/s/b
    name = models.CharField(max_length=255)


class Bazdid(models.Model):
    tour = models.ForeignKey(Tour)
    location_name = models.CharField(max_length=255)
    time = models.DateField()
    cost = models.IntegerField()


class Picture(models.Model):
    pict = models.FileField(upload_to="static/define_trip/img/", default="static/define_trip/img/default.jpg")
    gardesh = models.ForeignKey(Gardesh)


class AirPlane(models.Model):
    gardesh = models.ForeignKey(Gardesh, related_name='airplane')
    destination = models.CharField()    # city name
    source = models.CharField()         # city name
    start = models.DateField()
    start_t = models.TimeField()
    time = models.IntegerField()        # moddate parvaz
    capacity = models.IntegerField()    # number of un sell seats


class AirplaneSeat(models.Model):
    airplane = models.ForeignKey(AirPlane, related_name='seat')
    number = models.IntegerField()
    cost = models.IntegerField()        # gheimat ro joda begiram bara sandali ha?????
    full = models.BooleanField(default=False)


class Train(models.Model):
    gardesh = models.ForeignKey(Gardesh, related_name='airplane')
    destination = models.CharField()    # city name
    source = models.CharField()         # city name
    start = models.DateField()
    start_t = models.TimeField()
    time = models.IntegerField()        # moddate harekat
    capacity = models.IntegerField()    # number of un sell seats
    cost = models.IntegerField()


class TrainSeat(models.Model):
    train = models.ForeignKey(Train, related_name='seat')
    number = models.IntegerField()
    full = models.BooleanField(default=False)


class Restaurant(models.Model):
    gardesh = models.ForeignKey(Gardesh, related_name='restaurant')
    start_day = models.DateField()      # az che roozi bara foroosh mizari
    end_day = models.DateField()


class Table(models.Model):
    number = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant)
    capacity = models.IntegerField()    # zarfiate miz
    cost_perClock = models.IntegerField()


class TableReserve(models.Model):
    reserve_date = models.DateField()
    start_reserve = models.TimeField()
    end_reserve = models.TimeField()
    table = models.ForeignKey(Table)


class Hotel(models.Model):
    gardesh = models.ForeignKey(Gardesh, related_name='restaurant')
    start_day = models.DateField()      # az che roozi bara foroosh mizari
    end_day = models.DateField()


class Room(models.Model):
    number = models.IntegerField()
    hotel = models.ForeignKey(Hotel)
    capacity = models.IntegerField()    # zarfiate otagh
    cost_perNight = models.IntegerField()


class RoomReserve(models.Model):
    reserve_start = models.DateField()
    reserve_end = models.DateField()
    room = models.ForeignKey(Room)