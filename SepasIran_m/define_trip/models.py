from django.db import models
import datetime
from user.models import TourBuilderProfile


class Agreement(models.Model):
    percent = models.FloatField()    # between 0 and 1
    kind = models.CharField(max_length=30)   # tr-b /tr-s /tr-g/ a-b /...

KIND = (
    ('T', 'tour'),
    ('TR', ''),
    ('A', 'airplane'),
    ('H', 'hotel'),
    ('R', 'resturant'),
)
DEGREE = (
    ('G', 'golden'),
    ('S', 'silver'),
    ('B', 'bronze'),

)

T_KIND = (
    ('A', 'airplane'),
    ('T', 'train'),
    ('B', 'bus'),

)

L_KIND = (
    ('H', 'h'),
    ('A', 'a'),
    ('M', 'm'),

)
TOUR_KIND = (
    ('NAT', 'natrual'),
    ('INTER', 'international'),
    ('HOLLY', 'holly'),

)

class Gardesh(models.Model):
    builder = models.ForeignKey(TourBuilderProfile)
    kind = models.CharField(max_length=2,
                                      choices=KIND)   # t/tr/a/h/r
    final_rank = models.FloatField(null=True,blank=True)
    order_rank = models.FloatField(null=True,blank=True)
    comment_rank = models.FloatField(null=True,blank=True)
    degree = models.CharField(max_length=2,
                                      choices=DEGREE)     # g/s/b
    max_cancel_time = models.IntegerField(default= 2)
    free = models.FloatField(default=1)     # between 0 and 1 --> be nazaram inja darsad takhfif gozashte shavad behtar ast.
    define_time = models.DateTimeField(default= datetime.datetime.now)
    agreement = models.ForeignKey(Agreement)


class TransferDevice(models.Model):
    kind = models.CharField(max_length=2,
                                      choices=T_KIND)    # a/t/b
    degree = models.CharField(max_length=2,
                                      choices=DEGREE)      # g/s/b
    name = models.CharField(max_length=255)

class Location(models.Model):
    kind = models.CharField(max_length=2,
                                      choices=L_KIND)    # h/a/m
    degree = models.CharField(max_length=2,
                                      choices=DEGREE)      # g/s/b
    name = models.CharField(max_length=255)

class City(models.Model):
    name = models.CharField(max_length=255)

class Tour(models.Model):
    name = models.CharField(max_length=255)
    gardesh = models.ForeignKey(Gardesh, related_name='tour')
    tour_kind = models.CharField(max_length=30)      # nat / inter / holly
    destination = models.ForeignKey(City , related_name='tour_dest')    # city name
    source = models.ForeignKey(City , related_name='tour_source')         # city name
    start = models.DateField()
    start_t = models.TimeField()
    end = models.DateField()
    end_t = models.TimeField()
    capacity = models.IntegerField()    # tedadi ke mitavanim befrooshim
    has_sold = models.IntegerField(default=0)   # if = capacity or intire=0 => stop selling
    entire_capacity = models.IntegerField()     # mizani ke hanooz az zarfiate kol mande
    leader = models.CharField(max_length=30)
    leader_c = models.CharField(null=True, blank=True , max_length=50)
    transfer_device = models.ForeignKey(TransferDevice)
    stay_location = models.ForeignKey(Location)
    exclusive_cost = models.IntegerField()  # with out bazdid --> tour ha chenin apptioni gharar nemidan bara melat. age chizi mazad bar hazine bashe hamoonja khode mosafera hazine ash ro midan.
    entire_cost = models.IntegerField()
    destination_explain = models.TextField(null=True, blank=True)
    move_explain = models.TextField(null=True, blank=True)
    other_explain = models.TextField(null=True, blank=True)




class Bazdid(models.Model):
    tour = models.ForeignKey(Tour)
    location_name = models.CharField(max_length=255)
    time = models.DateField()
    cost = models.IntegerField()


class Picture(models.Model):
    pict = models.FileField(upload_to="static/define_trip/img/", default="static/define_trip/img/default.jpg")
    gardesh = models.ForeignKey(Gardesh)


class AirPlane(models.Model):
    name = models.CharField(max_length=100)
    gardesh = models.ForeignKey(Gardesh, related_name='airplane')
    destination = models.ForeignKey(City , related_name='airplain_dest')    # city name
    source = models.ForeignKey(City , related_name='airplain_source')         # city name
    start = models.DateField()
    start_t = models.TimeField()
    time = models.IntegerField()        # moddate parvaz
    capacity = models.IntegerField()    # number of un sell seats
    cost = models.IntegerField()


class AirplaneSeat(models.Model):
    airplane = models.ForeignKey(AirPlane, related_name='seat')
    number = models.IntegerField()
    full = models.BooleanField(default=False)


class Train(models.Model):
    name = models.CharField(max_length=100)
    gardesh = models.ForeignKey(Gardesh, related_name='train')
    destination = models.ForeignKey(City , related_name='train_dest')    # city name
    source = models.ForeignKey(City , related_name='train_source')         # city name
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
    name = models.CharField(max_length=100)
    gardesh = models.ForeignKey(Gardesh, related_name='restaurant')
    start_day = models.DateField()      # az che roozi bara foroosh mizari
    end_day = models.DateField()
    def __str__(self):
        return self.name#bug fixed by yeganeh


class Table(models.Model):
    number = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant)
    capacity = models.IntegerField()    # zarfiate miz
    cost_perClock = models.IntegerField()
    def __str__(self):
        #return str(self.restaurant) + str(self.number)#bug fixed by yeganeh
        return str(self.restaurant) + str(self.number)#bug fixed by yeganeh

class TableReserve(models.Model):
    reserve_date = models.DateField()
    start_reserve = models.TimeField()
    end_reserve = models.TimeField()
    table = models.ForeignKey(Table)
    def __str__(self):
        return str(self.table)

class Hotel(models.Model):
    name=models.CharField(max_length=100)
    gardesh = models.ForeignKey(Gardesh, related_name='hotel')
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