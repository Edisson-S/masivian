from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Roulette, Bet


class RouletteAdmin(admin.ModelAdmin):
    pass


class BetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Roulette, RouletteAdmin)
admin.site.register(Bet, BetAdmin)
