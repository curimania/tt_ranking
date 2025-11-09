from django.db import models
from players.models import Player

class Match(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    players_team1 = models.ManyToManyField(Player, related_name='team1_matches')
    players_team2 = models.ManyToManyField(Player, related_name='team2_matches')
    winner = models.IntegerField(choices=[(1, 'Team 1'), (2, 'Team 2')])

    def __str__(self):
        return f"Match {self.id} ({'Team 1' if self.winner == 1 else 'Team 2'} won)"
