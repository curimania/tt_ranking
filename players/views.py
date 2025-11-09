from django.shortcuts import render
from .models import Player

def ranking(request):
    players = Player.objects.order_by('-rating')
    return render(request, 'players/ranking.html', {'players': players})
