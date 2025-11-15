from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Match
from .logic import update_trueskill

def teams_ready(instance):
    """Prüft, ob beide Teams mind. einen Spieler haben."""
    return (
        instance.players_team1.count() > 0 and
        instance.players_team2.count() > 0
    )

@receiver(m2m_changed, sender=Match.players_team1.through)
@receiver(m2m_changed, sender=Match.players_team2.through)
def trigger_trueskill_after_teams_set(sender, instance, action, **kwargs):
    print(f"[SIGNAL] m2m_changed fired: {action}")

    # Wir brauchen das Signal NUR nach dem Hinzufügen von Spielern
    if action != "post_add":
        return

    # Prüfen ob beide Teams bereit sind
    if not teams_ready(instance):
        print("[SIGNAL] Teams noch nicht vollständig → kein Update")
        return

    # Schutz: TrueSkill nicht mehrfach berechnen
    if getattr(instance, "_trueskill_done", False):
        print("[SIGNAL] TrueSkill bereits berechnet → überspringe")
        return

    print("[SIGNAL] Berechne TrueSkill…")
    instance._trueskill_done = True   # interner Marker im RAM
    update_trueskill(instance)
    print("[SIGNAL] TrueSkill aktualisiert!")
