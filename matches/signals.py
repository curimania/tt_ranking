from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Match
from .logic import update_trueskill

@receiver(post_save, sender=Match)
def update_player_ratings(sender, instance, created, **kwargs):
    if created:
        update_trueskill(instance)
