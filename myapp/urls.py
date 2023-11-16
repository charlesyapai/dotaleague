from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.player_list, name='player_list'),
    # Add other URL patterns for myapp here
]
