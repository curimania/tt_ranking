from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)
    mu = models.FloatField(default=25.0)
    sigma = models.FloatField(default=8.333)
    rating = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        self.rating = self.mu - 3 * self.sigma
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.rating:.1f})"
