from django.contrib import admin
from .models import Sports,Teams,ScheduleCricket,PointsTableCricket


# Register your models here.
admin.site.register(Sports)
admin.site.register(Teams)
admin.site.register(ScheduleCricket)
admin.site.register(PointsTableCricket)
