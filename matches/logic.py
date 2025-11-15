import trueskill
from players.models import Player

env = trueskill.TrueSkill(draw_probability=0.01)

def update_trueskill(match):
    team1 = list(match.players_team1.all())
    team2 = list(match.players_team2.all())

    if not team1 or not team2:
        print("Teams unvollständig – SKIP")
        return

    # Aktuelle Ratings der Spieler laden
    team1_ratings = [p.get_trueskill_rating() for p in team1]
    team2_ratings = [p.get_trueskill_rating() for p in team2]

    # Gewinner bestimmen
    if match.winner == 1:
        ranks = [0, 1]  # Team1 gewinnt
    else:
        ranks = [1, 0]  # Team2 gewinnt

    # TrueSkill updaten
    new_team1, new_team2 = env.rate([team1_ratings, team2_ratings], ranks=ranks)

    # Neue Werte in Player-Modelle speichern
    for player, new_rating in zip(team1, new_team1):
        player.trueskill_mu = new_rating.mu
        player.trueskill_sigma = new_rating.sigma
        player.save()

    for player, new_rating in zip(team2, new_team2):
        player.trueskill_mu = new_rating.mu
        player.trueskill_sigma = new_rating.sigma
        player.save()

    print(">> TRUE SKILL erfolgreich aktualisiert")
