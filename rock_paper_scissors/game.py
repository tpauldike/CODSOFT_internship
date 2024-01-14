#!/usr/bin/env python3
# Play rock, paper, scissors on the command line
from game_module import RockPaperScissors as game
import time

current_game = game()

def play(player_choice):
        outcome = current_game.determine_the_winner(player_choice)
        if outcome:
            print(current_game.display_choice())
            print(outcome, end='\n\n')
        current_game.update_scores(outcome)
    
    
player = input("Enter your name: ")
if input(f"Welcome {player}! Press Enter to play or enter 'help' for help: ") == 'help':
    print()
    for char in game.display_help():
        print(char, end='', flush=True)
        time.sleep(0.08)
    print()
time.sleep(3)
while True:
    choice = input('\n' + game.prompt() + ': ')
    print()
    play(choice)
    print()
    if input("Press Enter to play again or 'q' to stop: ") == 'q':
        print('Bye!')
        break