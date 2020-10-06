from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Roulette


class NewRoulette(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = []

    def create(self, request, *args, **kwargs):
        roulette = Roulette.objects.create()
        reply = {"roulette_id": roulette.roulette_id}
        return Response(status=200, data=reply)
