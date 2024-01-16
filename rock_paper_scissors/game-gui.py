import tkinter as tk
import game_module as game

class GameGUI():
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry('600x400')
        self.root.title('Rock Paper Scissors')
        self.root.config(bg='#127E73')
        
        self.frame = tk.Label(self.root, bg='#DDDDDD')
        self.frame.pack(pady=50)
        
        self.score_board = tk.Label(self.frame, bg='#000000')
        self.score_board.pack()
        self.score_board.columnconfigure(2, weight=3)
        
        self.show_player_score = tk.Label(self.score_board, text='Your score\n0', font=('Serif', 11))
        self.show_player_score.grid(row=0, column=0)
        self.show_round = tk.Label(self.score_board, text='ROUND 1', font=('Arial', 20), padx=70)
        self.show_round.grid(row=0, column=1)
        self.show_comp_score = tk.Label(self.score_board, text="Computer\n0", font=('Serif', 11))
        self.show_comp_score.grid(row=0, column=2)
        
        self.root.mainloop()
        
GameGUI()