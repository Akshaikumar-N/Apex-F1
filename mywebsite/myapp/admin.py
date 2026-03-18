from django.contrib import admin
from .models import Team, Driver, Track, Rating, Prediction

admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Track)
admin.site.register(Rating)
admin.site.register(Prediction)
