import tkinter as tk
from tkinter import messagebox

primary_color = '#341234'

app = tk.Tk()
app.geometry('700x400')
app.title('Password Generator')

main_frame = tk.Label(app, height=350, width=650, bg=primary_color)
main_frame.pack(anchor='center', pady=20)

header = tk.Label(main_frame, text='pAsSwOrD gEneRatOr', bg="#000000", fg='#FFFFFF')
header.pack()

app.mainloop()