from django.db import models
import datetime
from user.models import TourBuilderProfile


class Agreement(models.Model):
    percent = models.FloatField()    # between 0 and 1
    kind = models.CharField(max_length=30)   # tr-b /tr-s /tr-g/ a-b /...

KIND = (
    ('T', 'تور'),
    ('TR', 'قطار'),
    ('A', 'هواپیما'),
    ('H', 'هتل'),
    ('R', 'رستوران'),
)
DEGREE = (
    ('G', 'طلایی'),
    ('S', 'نقره ای'),
    ('B', 'برنز'),

)

T_KIND = (
    ('A', 'هواپیما'),
    ('T', 'قطار'),
    ('B', 'اتوبوس'),

)

L_KIND = (
    ('H', 'هتل'),
    ('A', 'هتل آپارتمان'),
    ('M', 'مسافرخانه'),
    ('C', 'چادر'),

)
TOUR_KIND = (
    ('NAT', 'طبیعت گردی'),
    ('INTER', 'ایران گردی'),
    ('OUTER', 'جهان گردی'),
    ('HOLLY', 'زیارتی'),

)

CITY = (
    ('Tehran' , 'تهران'),
    ('Mashad' , 'مشهد'),
    ('Kish' , 'کیش'),
    ('Semnan' , 'سمنان'),
)

class Gardesh(models.Model):
    builder = models.ForeignKey(TourBuilderProfile)
    # kind = models.CharField(max_length=2,
    #                                   choices=KIND)   # t/tr/a/h/r copy to line:78
    final_rank = models.FloatField(null=True,blank=True)
    order_rank = models.FloatField(null=True,blank=True)
    comment_rank = models.FloatField(null=True,blank=True)
    degree = models.CharField(max_length=2,
                                      choices=DEGREE)     # g/s/b
    max_cancel_time = models.IntegerField(default= 2)
    free = models.FloatField(default=1)     # between 0 and 1 --> be nazaram inja darsad takhfif gozashte shavad behtar ast.
    define_time = models.DateTimeField(default= datetime.datetime.now)
    agreement = models.ForeignKey(Agreement)

    def __str__(self):
        return "{}".format(self.builder)


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

class Tour(models.Model):
    name = models.CharField(max_length=255)
    gardesh = models.ForeignKey(Gardesh, related_name='tour')
    kind = models.CharField(max_length=2,choices=KIND)   # t/tr/a/h/r
    tour_kind = models.CharField(max_length=30 , choices=TOUR_KIND)      # nat / inter / holly
    destination = models.CharField(max_length=255, choices=CITY)    # city name
    source = models.CharField(max_length=255,choices=CITY)         # city name
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
    entire_cost = models.IntegerField()
    destination_explain = models.TextField(null=True, blank=True)
    move_explain = models.TextField(null=True, blank=True)
    other_explain = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name#bug fixed by yeganeh




class Bazdid(models.Model):
    tour = models.ForeignKey(Tour)
    location_name = models.CharField(max_length=255)
    time = models.DateField()
    cost = models.IntegerField()


class Picture(models.Model):
    picture = models.FileField(upload_to="/static/define_trip/img/", default="/static/define_trip/img/default.jpg")
    gardesh = models.ForeignKey(Gardesh)


class AirPlane(models.Model):
    # name = models.CharField(max_length=100) #name hamoon name gardeshsaze nabayad dg in field bashe
    gardesh = models.ForeignKey(Gardesh, related_name='airplane')
    destination = models.CharField(max_length=255,choices=CITY)    # city name
    source = models.CharField(max_length=255,choices=CITY)         # city name
    start = models.DateField()
    start_t = models.TimeField()
    time = models.IntegerField()        # moddate parvaz
    capacity = models.IntegerField()    # number of un sell seats
    cost = models.IntegerField()
    def __str__(self):
        return self.name#bug fixed by yeganeh


class AirplaneSeat(models.Model):
    airplane = models.ForeignKey(AirPlane, related_name='seat')
    number = models.IntegerField()
    full = models.BooleanField(default=False)
    def __str__(self):
        #return str(self.restaurant) + str(self.number)#bug fixed by yeganeh
        return str(self.train) + str(self.number)#bug fixed by yeganeh


class Train(models.Model):
    # name = models.CharField(max_length=100) #name hamoon name gardeshsaze nabayad dg in field bashe
    gardesh = models.ForeignKey(Gardesh, related_name='train')
    destination = models.CharField(max_length=255,choices=CITY)    # city name
    source = models.CharField(max_length=255,choices=CITY)         # city name
    start = models.DateField()
    start_t = models.TimeField()
    time = models.IntegerField()        # moddate harekat
    capacity = models.IntegerField()    # number of un sell seats
    cost = models.IntegerField()
    def __str__(self):
        return str(self.name) + str(self.source) +'_' + str(self.destination)#bug fixed by yeganeh


class TrainSeat(models.Model):
    train = models.ForeignKey(Train, related_name='seat')
    number = models.IntegerField()
    full = models.BooleanField(default=False)
    def __str__(self):
        #return str(self.restaurant) + str(self.number)#bug fixed by yeganeh
        return str(self.train) + str(self.number)#bug fixed by yeganeh


class Restaurant(models.Model):
    # name = models.CharField(max_length=100) #name hamoon name gardeshsaze nabayad dg in field bashe
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
    # name=models.CharField(max_length=100) #name hamoon name gardeshsaze nabayad dg in field bashe
    gardesh = models.ForeignKey(Gardesh, related_name='hotel')
    start_day = models.DateField()      # az che roozi bara foroosh mizari
    end_day = models.DateField()
    other_explain = models.TextField(blank=True , null=True) #farzaneh add
    def __str__(self):
        return str(self.gardesh.builder.user.name)


class Room(models.Model):
    number = models.IntegerField()
    hotel = models.ForeignKey(Hotel)
    capacity = models.IntegerField()    # zarfiate otagh
    cost_perNight = models.IntegerField()
    full = models.BooleanField(default=False)
    def __str__(self):
        #return str(self.restaurant) + str(self.number)#bug fixed by yeganeh
        return str(self.hotel) + str(self.number)#bug fixed by yeganeh


class RoomReserve(models.Model):
    reserve_start = models.DateField()
    reserve_end = models.DateField()
    room = models.ForeignKey(Room)
    def __str__(self):
        return str(self.room)
