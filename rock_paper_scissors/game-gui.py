import tkinter as tk
import game_module as game

class GameGUI():
    
    def __init__(self) -> None:
        self.bg = '#227374'  # '#F0AE73'
        self.game_bg = '#432213'
        self.header_color = '#FFFFFF'
        
        self.root = tk.Tk()
        self.root.geometry('600x400')
        self.root.title('Rock Paper Scissors')
        self.root.config(bg=self.bg)
        
        self.frame = tk.Label(self.root, bg='#DDDDDD')
        self.frame.pack(pady=50)
        
        self.score_board = tk.Label(self.frame, bg=self.bg)
        self.score_board.pack()
        self.score_board.columnconfigure(2, weight=3)
        
        self.show_player_score = tk.Label(self.score_board, text='Your score\n0', font=('Serif', 11), bg=self.game_bg, fg=self.header_color, padx=10, pady=5)
        self.show_player_score.grid(row=0, column=0)
        self.show_round = tk.Label(self.score_board, text='ROUND 1', font=('Arial', 20, 'bold'), padx=70, bg=self.game_bg, fg=self.header_color)
        self.show_round.grid(row=0, column=1)
        self.show_comp_score = tk.Label(self.score_board, text="Computer\n0", font=('Serif', 11), bg=self.game_bg, fg=self.header_color, padx=10, pady=5)
        self.show_comp_score.grid(row=0, column=2)
        
        self.info_display = tk.Label(self.frame, font=('Arial', 13, 'italic'), height=10)
        self.info_display.pack()
        
        self.root.mainloop()
        
GameGUI()