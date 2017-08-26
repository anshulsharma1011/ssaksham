from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Apply,ApplyCricket,ApplyBadminton,ApplyFootball,ApplyAthletics,ApplyTugOfWar,ApplyBasketBall,ApplyVolleyBall,ApplyChess,ApplyCarrom,ApplyTableTennis

# Register your models here.

def selected(modeladmin,request,queryset):
    queryset.update(status='s')
selected.short_description="Mark selected students as Selected"

class ApplyAdmin(admin.ModelAdmin):
    list_display = ['user','status']
    ordering = ['user']
    actions = [selected]

admin.site.register(Apply,ApplyAdmin)
admin.site.register(ApplyCricket)
admin.site.register(ApplyBadminton)
admin.site.register(ApplyFootball)
admin.site.register(ApplyBasketBall)
admin.site.register(ApplyVolleyBall)
admin.site.register(ApplyChess)
admin.site.register(ApplyCarrom)
admin.site.register(ApplyTableTennis)
admin.site.register(ApplyTugOfWar)
admin.site.register(ApplyAthletics)

