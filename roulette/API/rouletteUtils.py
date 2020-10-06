from .models import Roulette, Bet
from rest_framework.authtoken.models import Token
import random


class RouletteUtils():
    def __init__(self):
        pass

    def get_status(self, roulette_id):
        roulette = Roulette.objects.filter(roulette_id=roulette_id)
        if len(roulette) > 0:
            return roulette[0].status
        else:
            return "NOT FOUND"

    def set_status(self, roulette_id, status):
        roulette = Roulette.objects.filter(roulette_id=roulette_id)
        if len(roulette) > 0:
            roulette = roulette[0]
            roulette.status = status
            roulette.save()
            return roulette.status
        else:
            return "ERROR"

    def get_results(self, roulette_id, action):
        winner_number, winner_color = self.get_winner(roulette_id, action)
        results = []
        bets = Bet.objects.filter(roulette_id=roulette_id)
        for bet in bets:
            result_bet = {}
            amount = bet.amount
            if bet.number == winner_number:
                result_bet["win"] = amount*5
            elif bet.number == winner_color:
                result_bet["win"] = amount*1.8
            else:
                result_bet["win"] = 0
            result_bet["user"] = Token.objects.get(key=bet.user).user.username
            result_bet["amount"] = bet.amount
            results.append(result_bet)

        return [results, winner_number]

    def get_winner(self, roulette_id, action):
        roulette = Roulette.objects.get(roulette_id=roulette_id)
        if action == "CLOSE":
            winner_number = random.randint(0, 36)
            roulette.winner_number = winner_number
            roulette.save()
        elif action == "LIST":
            winner_number = int(roulette.winner_number)

        if winner_number % 2:
            winner_color = "BLACK"
        else:
            winner_color = "RED"

        return [str(winner_number), winner_color]
