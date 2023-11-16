from django.db import models

# Example model
class Player(models.Model):
    name = models.CharField(max_length=100)
    mmr = models.IntegerField()

    def __str__(self):
        return self.name

# In myapp/models.py
class Player(models.Model):
    steam_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    mmr = models.IntegerField()
    # Add other relevant fields
