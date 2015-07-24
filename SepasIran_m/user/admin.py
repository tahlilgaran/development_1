from django.contrib import admin
from .models import TouristProfile,TourBuilderProfile,ManagerProfile

admin.site.register(TouristProfile)
admin.site.register(TourBuilderProfile)
admin.site.register(ManagerProfile)
