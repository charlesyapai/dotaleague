from django.db import models

# Example model
class Player(models.Model):
    name = models.CharField(max_length=100)
    mmr = models.IntegerField()

    def __str__(self):
        return self.name
