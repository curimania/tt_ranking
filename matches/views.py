from django.shortcuts import render, redirect
from .models import Match
from players.models import Player

def new_match(request):
    players = Player.objects.all()
    if request.method == 'POST':
        team1 = request.POST.getlist('team1')
        team2 = request.POST.getlist('team2')
        winner = int(request.POST['winner'])

        match = Match.objects.create(winner=winner)
        match.players_team1.set(Player.objects.filter(id__in=team1))
        match.players_team2.set(Player.objects.filter(id__in=team2))
        match.save()
        return redirect('ranking')

    return render(request, 'matches/match_form.html', {'players': players})
