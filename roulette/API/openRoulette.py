from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Roulette
from .rouletteUtils import RouletteUtils


class OpenRoulette(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = []

    def create(self, request, *args, **kwargs):
        roulette_utils = RouletteUtils()
        roulette_id = request.data["roulette_id"]
        roulette_status = roulette_utils.get_status(roulette_id)
        print("status:", roulette_status)
        if roulette_status == "NOT FOUND":
            reply = {"error": "Roulette does not exist"}
            response_status = 400
        elif (roulette_status != "NEW" and roulette_status != "CLOSED"):
            reply = {"error": "Roulette is already open"}
            response_status = 400
        else:
            new_status = roulette_utils.set_status(roulette_id, "OPEN")
            reply = {"status": new_status}
            response_status = 200

        return Response(status=response_status, data=reply)
