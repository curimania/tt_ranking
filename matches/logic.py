import trueskill
from players.models import Player

env = trueskill.TrueSkill(draw_probability=0.01)

def update_trueskill(match):
    team1 = list(match.players_team1.all())
    team2 = list(match.players_team2.all())

    ratings_team1 = [env.Rating(p.mu, p.sigma) for p in team1]
    ratings_team2 = [env.Rating(p.mu, p.sigma) for p in team2]

    if match.winner == 1:
        new_ratings = env.rate([ratings_team1, ratings_team2])
    else:
        new_ratings = env.rate([ratings_team2, ratings_team1])
        new_ratings = new_ratings[::-1]

    flat = new_ratings[0] + new_ratings[1]
    players = team1 + team2
    for player, rating in zip(players, flat):
        player.mu = rating.mu
        player.sigma = rating.sigma
        player.save()
