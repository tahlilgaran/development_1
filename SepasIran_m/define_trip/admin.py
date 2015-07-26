from django.contrib import admin
from .models import Hotel,Restaurant,Train,AirPlane,Agreement,AirplaneSeat,Bazdid,Gardesh,Picture,Location
from .models import TransferDevice,Room,RoomReserve,TrainSeat,Tour,Table,TableReserve

admin.site.register(TableReserve)
admin.site.register(Table)
admin.site.register(Tour)
admin.site.register(TrainSeat)
admin.site.register(Agreement)
admin.site.register(AirPlane)
admin.site.register(AirplaneSeat)
admin.site.register(Bazdid)
admin.site.register(Gardesh)
admin.site.register(Hotel)
admin.site.register(Train)
admin.site.register(Location)
admin.site.register(Picture)
admin.site.register(TransferDevice)
admin.site.register(Room)
admin.site.register(RoomReserve)
admin.site.register(Restaurant)
