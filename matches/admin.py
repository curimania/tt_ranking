from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'winner')
    filter_horizontal = ('players_team1', 'players_team2')
