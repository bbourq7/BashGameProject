from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game-list'),  # Example view for game_page
    path('add-game/', views.add_game, name='add_game'), 
    path('games/<int:pk>/', views.game_detail, name='game_detail'),
    path('games/<int:pk>/delete/', views.delete_game, name='delete-game'),
]