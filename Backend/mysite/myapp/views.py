from django.shortcuts import render
from .models import Player

# Example view
def player_list(request):
    players = Player.objects.all()
    return render(request, 'myapp/player_list.html', {'players': players})
