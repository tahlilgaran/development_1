from django.contrib import admin
from .models import Hotel,Restaurant,Train,AirPlane,Agreement,AirplaneSeat,Picture,Gardesh,Location
from .models import TransferDevice,Room,TrainSeat,Tour,Table

admin.site.register(Table)
admin.site.register(Tour)
admin.site.register(TrainSeat)
admin.site.register(Agreement)
admin.site.register(AirPlane)
admin.site.register(AirplaneSeat)
admin.site.register(Gardesh)
admin.site.register(Hotel)
admin.site.register(Train)
admin.site.register(Location)
admin.site.register(Picture)
admin.site.register(TransferDevice)
admin.site.register(Room)
admin.site.register(Restaurant)
