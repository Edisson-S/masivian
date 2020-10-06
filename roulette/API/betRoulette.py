from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Bet
from .rouletteUtils import RouletteUtils


class BetRoulette(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = []

    def create(self, request, *args, **kwargs):
        roulette_utils = RouletteUtils()
        userToken = request.headers["Authorization"]
        amount = request.data["amount"]
        number = request.data["number"]
        roulette_id = request.data["roulette_id"]
        roulette_status = roulette_utils.get_status(roulette_id)
        if int(number) > 36 or int(number) < 0:
            reply = {"error": "Invalid number, please try again"}
            response_status = 400
        elif amount > 10000:
            reply = {"error": "Bet exceeds the maximum amount"}
            response_status = 400
        elif roulette_status == "OPEN":
            bet = Bet.objects.create(
                amount=amount, roulette_id=roulette_id, number=number, user=userToken)
            bet.save()
            reply = {"status": "Bet Registered"}
            response_status = 200
        else:
            reply = {"error": "Incorrect roulette id"}
            response_status = 400
        return Response(status=response_status, data=reply)
