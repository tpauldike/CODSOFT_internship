import random

class RockPaperScissors():

    def __init__(self) -> None:
        self.player_choice = ''
        self.comp_choice = ''
        
        self.player_score = 0
        self.comp_score = 0
        
        self.options = ['rock', 'paper', 'scissors']

    def display_help() -> str:
        '''shows help for the game'''
        message ="The game is simple. You're to choose between 'rock', 'paper', and 'scissors' and the computer will as well choose."
        help = "The winner will be determined as soon as the both of you choose, it might be a tie as well."
        rule = "RULE: Rock beats scissors, scissors beat paper, and paper beats rock.\nYou are scored 3 for wins and 1 for draws"
        return f'{message}\n{help}\n{rule}\nHave fun!!'

    def prompt() -> str:
        '''prompts the user to play the game'''
        return 'Enter your choice or the number:\n1. Rock\n2. Paper\n3. Scissors\n'

    def determine_the_winner(self, player_choice: int | str) -> str | None:
        '''decides who won each round of the game'''
        try:
            player_choice = int(player_choice)
        except ValueError:
            if player_choice.lower() in self.options:
                player_choice = self.options.index(player_choice) + 1
            else:
                print(f"'{player_choice}' is invalid; type in rock, paper or scissors\n")
                return
            
        comp_choice = random.randint(1, 3)
        if player_choice <= 0 or player_choice > 3:
            print(f"'{player_choice}' is invalid; choose beetween 1, 2 and 3\n")
            return
        self.comp_choice = self.options[comp_choice-1]
        self.player_choice = self.options[player_choice-1]
        probable_outcome = {
            (1, 3): 'You win!',
            (3, 2): 'You win!',
            (2, 1): 'You win!',
            (3, 1): 'Computer wins!',
            (2, 3): 'Computer wins!',
            (1, 2): 'Computer wins!',
        }
        return probable_outcome.get((player_choice, comp_choice), "It's a tie")

    def display_choice(self) -> str:
        '''reveals the last choices made by the player and the computer'''
        if self.player_choice != '' and self.comp_choice != '':
            return f"Your choice: {self.player_choice.upper()}\nComputer's choice: {self.comp_choice.upper()}"

    def update_scores(self, outcome: str) -> None:
        '''Calculates the cummulative score after each round'''
        if outcome == 'You win!':
            self.player_score += 3
        elif outcome == 'Computer wins!':
            self.comp_score += 3
        elif outcome == "It's a tie":
            self.player_score += 1
            self.comp_score += 1
            
        print(f"Your current score: {self.player_score}")
        print(f"Computer's current score: {self.comp_score}")