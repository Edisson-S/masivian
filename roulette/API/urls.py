from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import User
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .newRoulette import NewRoulette
from .openRoulette import OpenRoulette
from .betRoulette import BetRoulette
from .createUser import CreateUser
from .closeRoulette import CloseRoulette
from .listroulette import ListRoulette

router = routers.DefaultRouter()
router.register(r'newroulette', NewRoulette, basename="new")
router.register(r'openroulette', OpenRoulette, basename="open")
router.register(r'betroulette', BetRoulette, basename="bet")
router.register(r'createuser', CreateUser, basename="newUser")
router.register(r'closeroulette', CloseRoulette, basename="close")
router.register(r'listroulette', ListRoulette, basename="close")

urlpatterns = [
    url(r'', include(router.urls)),
]
