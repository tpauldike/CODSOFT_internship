#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import sqlite3
import webbrowser
from lock_app import LockTodoApp


class TodoApp:

    def __init__(self) -> None:

        # VARIABLES FOR COLORS AND CONFIGURATIONS

        self.primary_color = '#AEB1B2'
        self.secondary_color = '#FFFFFF'
        self.color3 = '#1B1B32'
        self.highlighter = '#C9FFE3'
        self.highlighter2 = '#E86343'
        self.button_font = ('Times New Roman', 13)
        self.button_cnf = {'background': self.highlighter, 'font': self.button_font,
                           'activebackground': self.highlighter2, 'activeforeground': self.secondary_color, 'padx': 5}
        self.todo_list_cnf = {'width': 28, 'relief': 'groove', 'height': 20, 'anchor': 'nw',
                              'justify': 'left', 'padx': 15, 'pady': 17, 'activebackground': self.primary_color, 'fg': self.color3}
        self.menu_cnf = {'tearoff': 0, 'activebackground': self.highlighter2,
                         'activeforeground': self.secondary_color}
        self.default_notification_text = 'Welcome!\nNotifications are displayed here'
        self.sort_order = 'unsorted'

        self.root = tk.Tk()
        self.root.title('Todo App')

        # MENU SECTION

        self.menu = tk.Menu(self.root, bg=self.color3, bd=3, relief='groove',
                            fg=self.secondary_color, activebackground=self.highlighter, font=('Arial', 12))
        self.settings_menu = tk.Menu(
            self.menu, cnf=self.menu_cnf)
        self.sort_types = tk.Menu(self.settings_menu, cnf=self.menu_cnf)
        self.edit_menu = tk.Menu(self.menu, cnf=self.menu_cnf)
        self.help_menu = tk.Menu(self.menu, cnf=self.menu_cnf)
        self.contact_menu = tk.Menu(self.menu, cnf=self.menu_cnf)

        self.sort_types.add_command(
            label='Ascending order', command=lambda: self.sort_list('asc'))
        self.sort_types.add_command(
            label='Descending order', command=lambda: self.sort_list('desc'))

        self.settings_menu.add_command(label='Lock app', command=self.lock_app)
        self.settings_menu.add_cascade(label='Sort list', menu=self.sort_types)
        self.settings_menu.add_command(
            label='Show/hide', command=self.show_or_hide_list)
        self.settings_menu.add_command(
            label='Reminder', command=lambda: self.display_msg('Sorry!\nReminder menu is\ncurrently under maintenance'))
        self.settings_menu.add_command(
            label='Exit app', command=self.confirm_exit)

        self.edit_menu.add_command(
            label='Create new list', command=self.new_list)
        self.edit_menu.add_command(
            label='Edit single task', command=lambda: self.manage_task('Edit'))
        self.edit_menu.add_command(
            label='Delete task(s)', command=lambda: self.manage_task('Delete'))
        self.edit_menu.add_command(
            label='Delete all tasks', command=self.delete_all_tasks)

        self.help_menu.add_command(
            label='See README', command=lambda: self.open_in_browser('readme'))
        self.help_menu.add_command(
            label='Get Tutorial', command=lambda: self.open_in_browser('tutorial'))
        self.help_menu.add_command(
            label='via WhatsApp', command=lambda: self.open_in_browser('whatsapp'))

        self.contact_menu.add_command(
            label='Subscribe on YouTube', command=lambda: self.open_in_browser('youtube'))
        self.contact_menu.add_command(
            label='Follow on GitHub', command=lambda: self.open_in_browser('github'))
        self.contact_menu.add_command(
            label='Connect on LinkedIn', command=lambda: self.open_in_browser('linkedin'))
        self.contact_menu.add_command(
            label='Follow on Twitter', command=lambda: self.open_in_browser('twitter'))
        self.contact_menu.add_command(
            label='Connect on Facebook', command=lambda: self.open_in_browser('facebook'))

        self.menu.add_cascade(label='Settings', menu=self.settings_menu)
        self.menu.add_cascade(label='Edit', menu=self.edit_menu)
        self.menu.add_command(label='Search', command=self.search_list)
        self.menu.add_cascade(label='Get help', menu=self.help_menu)
        self.menu.add_cascade(label='Connect with Topman',
                              menu=self.contact_menu)

        self.root.config(menu=self.menu)
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)

        self.main_frame = tk.Frame(self.root, bg=self.primary_color)
        self.main_frame.pack(fill='x', pady=60)

        # lEFT SECTION (Todo list)

        self.todo_list = tk.Label(
            self.main_frame, font=('Open Sans', 12), cnf=self.todo_list_cnf)
        self.todo_list.grid(row=0, column=0, rowspan=12, padx=80, pady=30)

        # RIGHT SECTION (Entry fields, buttons and notification box)
        self.entry_fields = tk.Label(
            self.main_frame, width=35, relief='groove', height=12)
        self.entry_fields.grid(row=0, column=1, rowspan=6, padx=23, pady=30)

        self.prompt = tk.Label(
            self.entry_fields, text='Enter task here (32 characters, max): ', fg=self.color3, font=('Arial', 13))
        self.prompt.pack(pady=9, fill='both')

        # ENTRY FIELD FOR THE TASK
        self.task_field = tk.Entry(
            self.entry_fields, font=('Times New Roman', 13))
        self.task_field.pack(pady=10, padx=10, fill='both')

        self.checkbox_status = tk.IntVar()
        self.add_description = tk.Checkbutton(self.entry_fields, text='Add description', variable=self.checkbox_status,
                                              command=lambda: self.display_text_field(self.checkbox_status.get()), fg=self.color3)
        self.add_description.pack(pady=20)

        self.add_task_btn = tk.Button(
            self.entry_fields, text='Add task', cnf=self.button_cnf, command=self.add_task)
        self.add_task_btn.place(x=335, y=76)

        # OPTIONAL ENTRY FIELD FOR TASK DESCRIPTION
        self.description_field = tk.Text(
            self.entry_fields, font=self.button_font, height=3, width=40, state='disabled', highlightthickness=0)
        self.description_field.pack(pady=10, padx=10, fill='x')

        self.clear_btn = tk.Button(self.entry_fields, text='x', padx=1, pady=0, activebackground=self.highlighter2,
                                   activeforeground=self.secondary_color, state='disabled', command=self.clear_description_field)
        self.clear_btn.place(x=398, y=202)

        self.button_container = tk.Label(self.entry_fields)
        self.button_container.pack(fill='x', padx=13)

        # BUTTONS for LIST MANAGEMENT
        self.delete_task_btn = tk.Button(
            self.button_container, text='Delete task', cnf=self.button_cnf, command=lambda: self.manage_task('Delete'))
        self.delete_task_btn.grid(row=0, column=0, padx=5)
        self.edit_task_btn = tk.Button(
            self.button_container, text='Edit task', cnf=self.button_cnf, command=lambda: self.manage_task('Edit'))
        self.edit_task_btn.grid(row=0, column=1, padx=5)
        self.delete_list_btn = tk.Button(
            self.button_container, text='Delete list', cnf=self.button_cnf, command=self.delete_all_tasks)
        self.delete_list_btn.grid(row=0, column=2, padx=5)
        self.show_or_hide_btn = tk.Button(
            self.button_container, text='Show/hide', cnf=self.button_cnf, command=self.show_or_hide_list)
        self.show_or_hide_btn.grid(row=0, column=3, padx=5)

        self.notification_box = tk.Label(self.entry_fields, bg='#E5E7E9', fg='red',
                                         height=7, font=('Helvetica', 13))
        self.notification_box.pack(pady=10, fill='x', padx=13)

        # Set database if it is not set, else display the saved tasks
        self.set_up_database()
        self.display_todo_list()

        # Display default notification
        self.notification_box.after(
            1000, self.display_msg, self.default_notification_text)

        # Set the size and position of the window and start the app (loop infinitely)
        self.centralize_window(self.root, 1000, 650)
        self.root.mainloop()

    def add_task(self):
        try:
            task = self.task_field.get()
            description = self.description_field.get(1.0, tk.END)

            connection = sqlite3.connect("todo_list.db")
            if not task:
                self.display_msg("An empty task cannot be added")
                return

            characters = 0
            for c in task:
                characters += 1
            if characters > 32:
                self.display_msg(
                    "Error!\nA task cannot be more than\n32 characters long")
                return

            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO tasks (task, description) VALUES (?, ?)', (task, description))
            self.clear_task_field()
            self.clear_description_field()
            self.display_msg("Task successfully added")

        except sqlite3.Error as e:
            print(f"SQlite Error: {e}")
            self.display_msg('Oops!\nThere was an error with the database')
        finally:
            if connection:
                connection.commit()
                connection.close()

            self.display_todo_list()

    def manage_task(self, option):
        if not option or (option != 'Edit' and option != 'Delete'):
            print('option must be "Edit" or "Delete"')
            self.display_msg('Oh no!\nAn internal error occured')
            return
        self.create_temporary_label(option)

    def create_temporary_label(self, option):
        self.temporary_frame = tk.Frame(
            self.root, bg='lightgreen', width=820, height=400)
        self.temporary_frame.place(x=90, y=100)  # self.primary_color

        self.temporary_label = tk.LabelFrame(
            self.root, text='Manage Todo List', font=('Open Sans', 13), fg=self.color3)
        self.temporary_label.place(
            x=500, y=300, anchor=tk.CENTER, width=500, height=300)
        self.tasks_listed = tk.Listbox(self.temporary_label, selectforeground='red', selectbackground=self.highlighter, font=(
            'Open Sans', 12), selectmode=tk.SINGLE, height=150, relief='flat', bd=14, highlightthickness=0)
        self.tasks_listed.pack(fill='both', padx=5, pady=5)

        self.cancel_btn = tk.Button(
            self.temporary_label, cnf=self.button_cnf, text='Cancel', command=self.cancel_popup)
        self.cancel_btn.place(x=360, y=240)

        self.execute_btn = tk.Button(
            self.temporary_label, cnf=self.button_cnf, text=option, width=5)
        self.execute_btn.place(x=430, y=240)

        if option == 'Delete':
            self.tasks_listed.config(selectmode=tk.MULTIPLE)
            self.execute_btn.config(command=self.delete_tasks)
        elif option == 'Edit':
            self.tasks_listed.config(selectmode=tk.SINGLE)
            self.execute_btn.config(command=self.edit_task)

        try:
            connection = sqlite3.connect("todo_list.db")
            cursor = connection.cursor()

            if self.sort_order != 'unsorted':
                tasks = cursor.execute(
                    f"SELECT * FROM tasks ORDER BY task {self.sort_order}").fetchall()
            else:
                tasks = cursor.execute(f"SELECT * FROM tasks").fetchall()

            for task in tasks:
                self.tasks_listed.insert(tk.END, task[1])

        except sqlite3.Error as e:
            print(f"SQlite Error: {e}")
            self.display_msg(
                "Unknown Error!\nCheck the console if you're a developer")
        finally:
            connection.close()

    def destroy_temporary_label(self):
        self.temporary_label.destroy()
        self.temporary_frame.destroy()

    def restore_default(self):
        self.clear_task_field()
        self.clear_description_field()
        self.add_description.deselect()
        self.display_text_field(0)
        self.add_task_btn.config(text='Add task', command=self.add_task)

    def cancel_popup(self):
        self.destroy_temporary_label()
        self.restore_default()

    def delete_tasks(self):
        self.restore_default()
        try:
            selected_indices = self.tasks_listed.curselection()
            selected_tasks = [self.tasks_listed.get(
                task) for task in selected_indices]
            to_be_deleted = tuple(selected_tasks)

            connection = sqlite3.connect("todo_list.db")
            cursor = connection.cursor()
            placeholders = ', '.join(['?' for _ in to_be_deleted])
            cursor.execute(
                f"DELETE FROM tasks WHERE task IN ({placeholders})", to_be_deleted)

            self.destroy_temporary_label()

            row_count = cursor.rowcount
            if row_count <= 0:
                print('row count is less than 1')
                self.display_msg('Error!!\nNo task was selected')
                return
            elif row_count == 1:
                noun = 'task'
            else:
                noun = 'tasks'

            connection.commit()
            connection.close()

            self.display_todo_list()
            self.display_msg(f'{row_count} {noun} successfully deleted')
        except sqlite3.Error as e:
            print(f"SQlite Error: {e}")

    def edit_task(self):
        try:
            selected_task = self.tasks_listed.get(
                self.tasks_listed.curselection())

            connection = sqlite3.connect("todo_list.db")
            cursor = connection.cursor()
            self.task_to_update = cursor.execute(
                "SELECT * FROM tasks WHERE task=(?)", (selected_task,)).fetchone()

            self.clear_task_field()
            self.task_field.insert(0, self.task_to_update[1])

            self.clear_description_field()
            self.add_description.select()
            self.display_text_field(1)

            self.destroy_temporary_label()

            self.description_field.insert(1.0, self.task_to_update[2])
            self.add_task_btn.config(text='Update', command=self.update_task)
            if not self.task_to_update[2] or self.task_to_update[2] == '\n':
                self.display_msg('Oouch!\nNo description found for this task')
        except sqlite3.Error as e:
            print(f"SQlite Error: {e}")
        finally:
            connection.close()

    def update_task(self):
        try:
            task = self.task_field.get()
            description = self.description_field.get(1.0, tk.END)

            connection = sqlite3.connect("todo_list.db")
            if not task:
                self.display_msg("An empty task cannot be added")
                return

            characters = 0
            for c in task:
                characters += 1
            if characters > 32:
                self.display_msg(
                    "Error!\nA task cannot be more than\n32 characters long")
                return

            cursor = connection.cursor()
            cursor.execute(
                'UPDATE tasks SET task=(?), description=(?) WHERE task=(?) ', (task, description, self.task_to_update[1]))

            self.restore_default()
            self.display_msg("Task successfully updated")

        except sqlite3.Error as e:
            print(f"SQlite Error: {e}")
            self.display_msg('Oops!\nThere was an error with the database')
        finally:
            if connection:
                connection.commit()
                connection.close()

            self.display_todo_list()

    def search_list(self):
        self.display_msg('Search is not available yet')

    def delete_all_tasks(self):
        self.restore_default()
        choice = messagebox.askokcancel(
            title="Delete all?", message="The current list will be entirely lost and this can not be undone. Do you want to continue?")
        if choice == True:
            connection = sqlite3.connect("todo_list.db")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM tasks")
            connection.commit()
            connection.close()
            self.display_msg('Successfully deleted the list')
            self.display_todo_list()
        if choice == False:
            self.display_msg('Operation canceled')
        else:
            self.display_msg('Oops!\nAn unknown error occured')

    def sort_list(self, order):

        connection = sqlite3.connect("todo_list.db")
        cursor = connection.cursor()

        if order == 'asc' and self.sort_order != 'ASC':
            tasks = cursor.execute(
                "SELECT * FROM tasks ORDER BY task ASC").fetchall()
            self.sort_order = 'ASC'
            self.display_msg('List sorted in ascending order')

        elif order == 'desc' and self.sort_order != 'DESC':
            tasks = cursor.execute(
                "SELECT * FROM tasks ORDER BY task DESC").fetchall()
            self.sort_order = 'DESC'
            self.display_msg('List sorted in descending order')
        else:
            self.display_todo_list()
            self.sort_order = 'unsorted'
            self.display_msg('List sorted by time added')
            return

        sorted_list = "\n".join(
            [f"{i + 1}. {task[1]}" for i, task in enumerate(tasks)])
        self.todo_list.config(text=sorted_list)
        connection.close()

    def new_list(self):
        choice = messagebox.showwarning(
            title='One list per time', message='You can only have one list per time, a new one requires deleting the existing one')
        if choice == 'ok':
            self.delete_all_tasks()

    def show_or_hide_list(self):
        if self.todo_list.cget('text') == "":
            self.display_todo_list()
            self.display_msg('List visible')
        else:
            self.todo_list.config(text="")
            self.display_msg('List hidden.\nClick on "show" to see list')

    def display_text_field(self, checkbox_status):
        if checkbox_status == 1:
            self.description_field.config(state='normal', highlightthickness=1)
            self.clear_btn.config(state='active')
        else:
            self.clear_description_field()
            self.description_field.config(
                state='disabled', highlightthickness=0)
            self.clear_btn.config(state='disabled')

    def clear_task_field(self):
        self.task_field.delete(0, tk.END)

    def clear_description_field(self):
        self.description_field.delete(1.0, tk.END)

    def set_up_database(self):
        try:
            connection = sqlite3.connect("todo_list.db")
            cursor = connection.cursor()
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        except sqlite3.Error as e:
            print("Sqlite Error: {}".format(e))
        finally:
            if connection:
                connection.commit()
                connection.close()

    def display_todo_list(self):
        connection = sqlite3.connect("todo_list.db")
        cursor = connection.cursor()
        tasks = cursor.execute("SELECT * FROM tasks").fetchall()

        if not tasks:
            self.todo_list.config(text="Empty Todo List",
                                  anchor='center', fg=self.highlighter2)
        else:
            tasks_list = "\n".join(
                [f"{i + 1}. {task[1]}" for i, task in enumerate(tasks)])
            self.todo_list.config(text=tasks_list, cnf=self.todo_list_cnf)

        connection.close()

    def display_msg(self, msg):
        if not msg:
            msg = ""

        self.notification_box.config(text=msg)

        if msg == "":
            return
        self.notification_box.after(3000, self.display_msg, "")

    def confirm_exit(self):
        option = messagebox.askyesno(
            title='Confirm Exit', message='Do you really want to exit the app?')
        if option == 1:
            self.root.quit()

    def open_in_browser(self, platform):
        web_url = {
            'readme': 'https://github.com/tpauldike/CODSOFT/blob/main/to-do_list/README.md',
            'tutorial': 'https://youtube.com/@tpauldike',
            'whatsapp': 'https://wa.link/66ef36',
            'youtube': 'https://youtube.com/@tpauldike',
            'github': 'https://github.com/tpauldike',
            'linkedin': 'https://linkedin.com/in/tpauldike',
            'twitter': 'https://twitter.com/tpauldike',
            'facebook': 'https://facebook.com/tpauldike'
        }
        webbrowser.open(web_url[platform])
        
    def centralize_window(self, window: object, width: int, height: int):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{str(width)}x{str(height)}+{x}+{y}")
    
    def lock_app(self):
        LockTodoApp(self.root)
 

TodoApp()
