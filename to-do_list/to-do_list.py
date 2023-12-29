import tkinter as tk
from tkinter import messagebox
import sqlite3


class TodoApp:

    def __init__(self) -> None:

        # VARIABLES FOR COLORS AND CONFIGURATIONS

        self.primary_color = '#AEB1B2'
        self.secondary_color = '#FFFFFF'
        self.color3 = '#1B1B32'
        self.highlighter = '#C9FFE3'
        self.highlighter2 = '#E86343'
        self.button_font = ('Times New Roman', 13)
        self.button_cfn = {'background': self.highlighter, 'font': self.button_font,
                           'activebackground': self.highlighter2, 'activeforeground': self.secondary_color, 'padx': 5}

        self.root = tk.Tk()
        self.root.title('Todo App')
        self.root.geometry('1000x650')
        
        # MENU SECTION

        self.menu = tk.Menu(self.root, bg=self.color3, bd=3, relief='groove',
                            fg=self.secondary_color, activebackground=self.highlighter, font=('Arial', 12))
        self.settings_menu = tk.Menu(
            self.menu, tearoff=0, activebackground=self.highlighter2, activeforeground=self.secondary_color)
        self.sort_types = tk.Menu(self.settings_menu, tearoff=0,
                                  activebackground=self.highlighter2, activeforeground=self.secondary_color)
        self.edit_menu = tk.Menu(
            self.menu, tearoff=0, activebackground=self.highlighter2, activeforeground=self.secondary_color)

        self.sort_types.add_command(
            label='Ascending order', command=self.sort_list)
        self.sort_types.add_command(
            label='Descending order', command=self.sort_list)

        self.settings_menu.add_command(label='Lock app', command=self.lock_app)
        self.settings_menu.add_cascade(label='Sort list', menu=self.sort_types)
        self.settings_menu.add_command(
            label='Show/hide', command=self.show_or_hide_list)
        self.settings_menu.add_command(
            label='Exit app', command=self.confirm_exit)

        self.edit_menu.add_command(
            label='Create new list', command=self.new_list)
        self.edit_menu.add_command(
            label='Edit one task', command=self.edit_task)
        self.edit_menu.add_command(
            label='Delete one task', command=self.delete_one_task)
        self.edit_menu.add_command(
            label='Delete all tasks', command=self.delete_all_tasks)

        self.menu.add_cascade(label='Settings', menu=self.settings_menu)
        self.menu.add_cascade(label='Edit', menu=self.edit_menu)
        self.menu.add_command(label='Search', command=self.search_list)
        self.root.config(menu=self.menu)
        # self.root.protocol("WM_DELETE_WINDOW", confirm_exit)

        self.main_frame = tk.Frame(self.root, bg=self.primary_color)
        self.main_frame.pack(fill='x', pady=60)

        # lEFT SECTION (Todo list)

        self.todo_list = tk.Label(
            self.main_frame, width=40, relief='groove', height=25)
        self.todo_list.grid(row=0, column=0, rowspan=12, padx=70, pady=30)

        # RIGHT SECTION (Entry fields, buttons and notification box)
        self.entry_fields = tk.Label(
            self.main_frame, width=35, relief='groove', height=12)
        self.entry_fields.grid(row=0, column=1, rowspan=6, padx=40, pady=30)

        self.prompt = tk.Label(
            self.entry_fields, text='Enter new task here: ', fg=self.color3)
        self.prompt.pack(pady=10, fill='both')

        # ENTRY FIELD FOR THE TASK
        self.task_field = tk.Entry(
            self.entry_fields, font=('Times New Roman', 13))
        self.task_field.pack(pady=10, padx=10, fill='both')

        self.checkbox_status = tk.IntVar()
        self.add_description = tk.Checkbutton(self.entry_fields, text='Add description', variable=self.checkbox_status,
                                              command=lambda: self.display_text_field(self.checkbox_status.get()), fg=self.color3)
        self.add_description.pack(pady=20)

        self.add_task_btn = tk.Button(
            self.entry_fields, text='Add task', cnf=self.button_cfn)
        self.add_task_btn.place(x=335, y=76)

        # OPTIONAL ENTRY FIELD FOR TASK DESCRIPTION
        self.description_field = tk.Text(
            self.entry_fields, font=self.button_font, height=3, width=40, state='disabled')
        self.description_field.pack(pady=10, padx=10, fill='x')

        self.button_container = tk.Label(self.entry_fields)
        self.button_container.pack(fill='x', padx=13)

        # BUTTONS for LIST MANAGEMENT
        self.delete_task_btn = tk.Button(
            self.button_container, text='Delete task', cnf=self.button_cfn)
        self.delete_task_btn.grid(row=0, column=0, padx=5)
        self.edit_task_btn = tk.Button(
            self.button_container, text='Edit task', cnf=self.button_cfn)
        self.edit_task_btn.grid(row=0, column=1, padx=5)
        self.delete_list_btn = tk.Button(
            self.button_container, text='Delete list', cnf=self.button_cfn)
        self.delete_list_btn.grid(row=0, column=2, padx=5)
        self.show_or_hide_btn = tk.Button(
            self.button_container, text='Show/hide', cnf=self.button_cfn)
        self.show_or_hide_btn.grid(row=0, column=3, padx=5)

        self.notification_box = tk.Label(self.entry_fields, bg=self.secondary_color, fg=self.color3,
                                         height=7, text='Trying to test. Let\'s see how this works.\nTesting', font=('Helvetica', 13))
        self.notification_box.pack(pady=10, fill='x', padx=13)
        
        # SET DATABASE IF IT IS NOT SET, ELSE DISPLAY THE SAVED TASKS
        self.set_up_database()
        self.display_todo_list()

        self.root.mainloop()

    def add_task(self):
        task = self.task_field.get()
        description = self.description_field.get()
        
        connection = sqlite3.connect("todo_list.db")
        cursor = connection.cursor()
        cursor.execute('INSERT INTO tasks (task, description) VALUES (?, ?)', (task, description))
        connection.commit()
        connection.close()
        
        self.task_field.destroy()
        self.description_field.destroy()
        self.display_todo_list()

    def edit_task():
        pass

    def delete_one_task():
        pass

    def search_list():
        pass

    def delete_all_tasks():
        pass

    def sort_list():
        pass

    def new_list():
        pass

    def show_or_hide_list():
        pass

    def display_text_field(self, checkbox_status):
        if checkbox_status == 1:
            self.description_field.config(state='normal')
        else:
            self.description_field.config(state='disabled')

    def lock_app():
        pass

    def set_up_database(self):
        connection = sqlite3.connect("todo_list.db")
        cursor = connection.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS tasks (
                           id INTEGER PRIMARY KEY,
                           task TEXT,
                           description TEXT
                       )
                       ''')
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS lock_password (
                           lock_password TEXT,
                           locked BOOLEAN
                       )
                       ''')
        connection.commit()
        connection.close()

    def display_todo_list(self):
        connection = sqlite3.connect("todo_list.db")
        cursor = connection.cursor()
        tasks = cursor.execute("SELECT * FROM tasks").fetchall()
        
        number = 1
        for task in tasks:
            self.todo_list.insert(tk.END, str(number) + '. ' + task[0] + '\n')
            number += 1
    
        connection.close()
            
    def confirm_exit(self):
        option = messagebox.askyesno(
            title='Confirm Exit', message='Do you really want to exit the app?')
        if option == 1:
            self.root.quit()


TodoApp()

# d0d0f5 lightgreen #355e64 #e86343  height=500, width=850, , image='./images/app_icon.ico'
