import tkinter as tk
from tkinter import messagebox

class LockTodoApp:
    def __init__(self, root):
        self.root = root
        
        self.popup = tk.Toplevel()
        self.popup.title('Lock App')
        self.popup.config(bg='lightblue')
        self.centralize_window(self.popup, 600, 400)
        self.popup.transient(self.root)
        self.popup.grab_set()
        
        # Global Variables
        self.submit_btn_text = "Enter"
        self.pswd_label_text = 'Set Your Password'
        label_cnf = {'text': self.pswd_label_text,'labelanchor': 'n', 'padx': 10, 'pady': 10}
        self.highlighter = '#C9FFE3'
        self.highlighter2 = '#E86343'
        self.button_font = ('Times New Roman', 13)
        self.button_cnf = {'background': self.highlighter, 'font': self.button_font,
                           'activebackground': self.highlighter2, 'activeforeground': '#FFFFFF', 'padx': 5, 'width': 16, 'pady': 1}
        pswd = tk.StringVar()
        use_pswd = tk.BooleanVar()
        
        self.pswd_label = tk.LabelFrame(self.popup, cnf=label_cnf, font= ("Arial", 13))
        self.pswd_label.pack(anchor='center', pady=150)
        
        self.pswd_field = tk.Entry(self.pswd_label, textvariable=pswd, width=40, show='*')
        self.pswd_field.pack()
        
        self.btn_container = tk.Label(self.pswd_label, pady=10)
        self.btn_container.pack()
        
        self.cancel_btn = tk.Button(self.btn_container, text='Cancel', cnf=self.button_cnf, command=self.close_popup)
        self.cancel_btn.grid(row=0, column=0)
        
        self.submit_btn = tk.Button(self.btn_container, text=self.submit_btn_text, cnf=self.button_cnf, command=self.under_maintenance_error)
        self.submit_btn.grid(row=0, column=1)
        
        self.root.mainloop()
        
    def centralize_window(self, window: object, width: int, height: int):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{str(width)}x{str(height)}+{x}+{y}")
        
    def close_popup(self):
        self.popup.destroy()
    
    def new_password():
        pass
    
    def under_maintenance_error(self):
        self.close_popup()
        messagebox.showerror(title='Sorry!', message='This functionality is currently under maintenance')
    
    def change_password():
        pass

    def lock_app(self):
        pass
    