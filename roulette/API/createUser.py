
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User


class CreateUser(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = []

    def create(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        User.objects.create(username=username, password=password)
        reply = {"status": "user created successfully"}

        return Response(status=200, data=reply)
