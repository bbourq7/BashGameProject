from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from .forms import GameForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def add_game(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print(request.FILES)
            
            game = form.save()  # Save the form and get the saved game object
            game.unzip_file()  # Call the unzip_file method
            return redirect('game-list')
    else:
        form = GameForm()
    return render(request, 'game_files/add_game.html', {'form': form})

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_files/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    print(f"Game ID: {game.id}")
    print(f"Game Name: {game.name}")
    print(f"Game Description: {game.description}")
    print(f"Game File: {game.game_file}")
    print(game.game_file) 
    return render(request, 'game_files/game_detail.html', {'game': game})

@login_required
def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.delete()
        messages.success(request, 'Game deleted successfully!')
        return redirect('game-list')  # Redirect to the list of games or any other page
    return render(request, 'game_files/confirm_game_delete.html', {'game': game})
