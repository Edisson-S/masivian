from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
import uuid
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Roulette(models.Model):
    roulette_id = models.CharField(
        max_length=50, unique=True, default=uuid.uuid4)
    status = models.CharField(max_length=10, blank=True, default="NEW")
    winner_number = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return "Roulette"


class Bet(models.Model):
    amount = models.IntegerField(null=True, blank=True)
    roulette_id = models.CharField(max_length=50)
    number = models.CharField(max_length=5, null=True, blank=True)
    user = models.CharField(max_length=50)

    def __str__(self):
        return "Bet"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
