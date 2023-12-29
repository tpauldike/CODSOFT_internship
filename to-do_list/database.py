import tkinter as tk

root = tk.Tk()
root.title('My Application')

primary_color = 'lightblue'

main_frame = tk.Frame(root, height=500, width=850, bg=primary_color)
main_frame.pack(fill='x', pady=60)

enter = tk.Entry(main_frame)
enter.pack()

root.mainloop()
