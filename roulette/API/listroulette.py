from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Roulette, Bet
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .rouletteUtils import RouletteUtils
import random


class ListRoulette(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = []

    def create(self, request, *args, **kwargs):
        roulette_utils = RouletteUtils()
        roulette_id = request.data["roulette_id"]
        roulette_status = roulette_utils.get_status(roulette_id)
        if roulette_status == "NOT FOUND":
            reply = {"error": "Roulette does not exist"}
            response_status = 400
        elif roulette_status == "OPEN":
            reply = {"error": "Roulette still open"}
            response_status = 400
        else:
            [results, winner_number] = roulette_utils.get_results(
                roulette_id, "LIST")
            reply = {"winner_number": winner_number, "results": results}
            response_status = 200

        return Response(status=response_status, data=reply)
