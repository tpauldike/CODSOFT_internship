import tkinter as tk
from tkinter import messagebox
import webbrowser
from arithmetics import Caculator
import re


class GUI:
    '''Instatiates the Graphical User Interface of a calculator'''

    def __init__(self):
        self.background_color = '#114234'
        self.color2 = '#80B6B6'
        self.color3 = '#FFFFFF'
        self.color4 = '#2CDDD1'
        self.root_bg = '#000000'
        self.display_bg = '#238A83'
        self.faded_black = '#333333'

        self.top_btn_cnf = {'width': 5, 'bg': self.color2, 'fg': self.root_bg,
                            'activebackground': self.color2, 'activeforeground': self.faded_black}
        self.num_btn_cnf = {'width': 6, 'bg': self.color4, 'fg': self.background_color, 'font': (
            'Lucida', 16), 'activebackground': self.display_bg, 'activeforeground': self.color3}
        self.math_btn_cnf = {'width': 8, 'bg': self.background_color, 'fg': self.color3, 'font': (
            'Cambria', 12, 'italic'), 'activebackground': self.display_bg, 'activeforeground': self.color3}

        self.help_text = """
  Press:
    Enter for 'equals',  Esc for 'clear',
    Alt/Meta (right) for 'answer',  '/' for '÷',
    Backspace for '←',  Shift+8 (*) for '×'
        """

        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.config(bg='#000000')
        self.centralize_window(self.root, 800, 600)

        # Main frame and display screen
        self.main_frame = tk.Label(
            self.root, pady=20, padx=10, bg=self.background_color)
        self.main_frame.pack(pady=40, padx=10)

        self.display = tk.Entry(self.main_frame, font=('Garamond', 20), justify='right', highlightthickness=0,
                                readonlybackground=self.display_bg, bg=self.display_bg, fg=self.color3, state='readonly')
        self.display.pack(pady=20, padx=10, fill='none')
        self.last_answer = '0'
        self.default_display = '0'

        # Buttons at the top
        self.top_btn_cont = tk.Label(self.main_frame, bg=self.background_color)
        self.top_btn_cont.pack()
        self.power_btn = tk.Button(
            self.top_btn_cont, text='on', cnf=self.top_btn_cnf, command=self.power_switch)
        self.power_btn.grid(row=0, column=0)
        self.answer_btn = tk.Button(
            self.top_btn_cont, text='answer', cnf=self.top_btn_cnf, command=self.show_last_ans)
        self.answer_btn.grid(row=0, column=1)
        self.clear_btn = tk.Button(
            self.top_btn_cont, text='clear', cnf=self.top_btn_cnf, command=self.clear)
        self.clear_btn.grid(row=0, column=2)
        self.back_btn = tk.Button(
            self.top_btn_cont, text='←', cnf=self.top_btn_cnf, command=self.delete_last_char)
        self.back_btn.grid(row=0, column=3)
        self.elipse_btn = tk.Button(
            self.top_btn_cont, text='...', cnf=self.top_btn_cnf, command=self.display_info)
        self.elipse_btn.grid(row=0, column=4)

        # Button container and the buttons
        self.btn_container = tk.Label(
            self.main_frame, bg=self.color3, pady=10, padx=0)
        self.btn_container.pack(pady=10)
        self.btn_container.columnconfigure(0, weight=1)
        self.btn_container.columnconfigure(1, weight=1)
        self.btn_container.rowconfigure(3, weight=1)
        self.create_number_btns()
        self.create_math_btns()

        # Help section for using the keyboard
        self.keys_help = tk.Label(self.root, bg=self.root_bg, fg=self.color3,
                                  text=self.help_text, justify='left', font=('Verdana', 12, 'italic'))
        self.keys_help.pack(anchor='center')

        # Power on the calculator and start the infinite loop
        self.power_switch()
        self.root.bind('<KeyPress>', self.check_valid_char)
        self.root.mainloop()

    def centralize_window(self, window: object, width: int, height: int):
        '''Positions the display window to the center of the screen'''
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{str(width)}x{str(height)}+{x}+{y}")

    def create_number_btns(self):
        '''Creates the number buttons (0-9)'''
        self.btn_1 = tk.Button(self.btn_container, text='1',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('1'))
        self.btn_1.grid(row=0, column=0)
        self.btn_2 = tk.Button(self.btn_container, text='2',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('2'))
        self.btn_2.grid(row=0, column=1)
        self.btn_3 = tk.Button(self.btn_container, text='3',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('3'))
        self.btn_3.grid(row=0, column=2)
        self.btn_4 = tk.Button(self.btn_container, text='4',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('4'))
        self.btn_4.grid(row=1, column=0)
        self.btn_5 = tk.Button(self.btn_container, text='5',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('5'))
        self.btn_5.grid(row=1, column=1)
        self.btn_6 = tk.Button(self.btn_container, text='6',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('6'))
        self.btn_6.grid(row=1, column=2)
        self.btn_7 = tk.Button(self.btn_container, text='7',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('7'))
        self.btn_7.grid(row=2, column=0)
        self.btn_8 = tk.Button(self.btn_container, text='8',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('8'))
        self.btn_8.grid(row=2, column=1)
        self.btn_9 = tk.Button(self.btn_container, text='9',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('9'))
        self.btn_9.grid(row=2, column=2)
        self.btn_0 = tk.Button(self.btn_container, text='0',
                               cnf=self.num_btn_cnf, command=lambda: self.display_char('0'))
        self.btn_0.grid(row=3, column=2)

    def create_math_btns(self):
        '''Creates the buttons with mathematical expressions'''
        self.plus_btn = tk.Button(self.btn_container, text='+',
                                  cnf=self.math_btn_cnf, command=lambda: self.display_sign('+'))
        self.plus_btn.grid(row=3, column=0, sticky='news')
        self.minus_btn = tk.Button(
            self.btn_container, text='-', cnf=self.math_btn_cnf, command=lambda: self.display_sign('-'))
        self.minus_btn.grid(row=3, column=1, sticky='news')
        self.times_btn = tk.Button(
            self.btn_container, text='×', cnf=self.math_btn_cnf, command=lambda: self.display_sign('×'))
        self.times_btn.grid(row=4, column=0, sticky='news')
        self.div_btn = tk.Button(self.btn_container, text='÷',
                                 cnf=self.math_btn_cnf, command=lambda: self.display_sign('÷'))
        self.div_btn.grid(row=4, column=1, sticky='news')
        self.dot_btn = tk.Button(self.btn_container, text='.',
                                 cnf=self.math_btn_cnf, command=lambda: self.display_once('.'))
        self.dot_btn.grid(row=5, column=0, sticky='news')
        self.negative_btn = tk.Button(
            self.btn_container, text='±', cnf=self.math_btn_cnf, command=self.display_minus)
        self.negative_btn.grid(row=5, column=1, sticky='news')
        self.equals_btn = tk.Button(self.btn_container, text='=', bg=self.color2, font=(
            'Cambria', 15), activebackground=self.color2, activeforeground=self.faded_black, command=self.evaluate)
        self.equals_btn.grid(row=4, column=2, rowspan=2, sticky='news')

        self.sqrd_btn = tk.Button(
            self.btn_container, text='x²', cnf=self.math_btn_cnf, command=self.square)
        self.sqrd_btn.grid(row=6, column=0, sticky='news')
        self.powr_btn = tk.Button(self.btn_container, text='^',
                                  cnf=self.math_btn_cnf, command=lambda: self.display_once('^'))
        self.powr_btn.grid(row=6, column=1, sticky='news')
        self.sqrt_btn = tk.Button(
            self.btn_container, text='√', cnf=self.math_btn_cnf, command=self.square_root_of)
        self.sqrt_btn.grid(row=6, column=2, sticky='news')

    def display_char(self, char):
        '''Displays char on the calculator's screen'''
        current_str = self.display.get()
        if current_str:
            if current_str == '0' or str(self.last_answer) == current_str:
                self.display.delete(0, tk.END)
        self.display.insert(tk.END, char)

    def display_once(self, char):
        '''Displays a character only once, if it is not already in the substring delimited by "+-÷×"'''
        current_str = self.display.get()
        last_substring = re.split('[+|\-|÷|×]', current_str)[-1]
        if (char == '^' and current_str == '0') or (current_str[-1] in '+-÷×'):
            return
        for i in last_substring:
            if i == char:
                return
        self.display.insert(tk.END, char)

    def display_minus(self):
        '''Toggles between displaying minus before the number and taking it off'''
        current_str = self.display.get()
        prepend_minus = '-' + current_str
        if current_str and current_str != '0':
            if current_str[0] != '-':
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, prepend_minus)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, current_str[1:])

    def display_sign(self, sign):
        current_str = self.display.get()
        if current_str[-1] in '+-÷×.^':
            self.delete_last_char()
        elif current_str == '0':
            return
        if sign == '/':
            sign = '÷'
        elif sign == '*':
            sign = '×'
        self.display.insert(tk.END, sign)

    def clear(self):
        '''Clears the calculator's screen and displays zero (0)'''
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, '0')

    def delete_last_char(self):
        '''Deletes the last characted entered'''
        current_str = self.display.get()
        if current_str:
            new_str = current_str[0:-1]
            self.display.delete(0, tk.END)
            if len(current_str) == 1:
                new_str = '0'
            self.display_char(new_str)

    def power_switch(self):
        '''Powers the caculator on if off, and off if on, with the option to exit the app'''
        if self.display.cget('state') == 'normal' and self.power_btn.cget('text') == 'off':
            self.display.delete(0, tk.END)
            self.display.config(state='readonly')
            self.power_btn.config(text='on', activeforeground='green')
        else:
            self.default_display = '0'
            self.display.config(state='normal')
            self.power_btn.config(
                text='off', activeforeground='red', activebackground='white')
            self.clear()

    def show_last_ans(self):
        '''Displays the very last answer produced'''
        current_str = self.display.get()
        if str(self.last_answer) == current_str or str(self.last_answer) == '0':
            return
        elif current_str[-1] in '+-*/^÷×':
            self.display.insert(tk.END, self.last_answer)
        else:
            messagebox.showwarning(
                title='Invalid Operation', message='Enter +, -, ÷, × or ^ before you press answer')

    def display_info(self):
        messagebox.showinfo(title='Under Maintenance',
                            message='This feature is currently under maintenance')
        response = messagebox.askquestion(
            title='See Source Code?', message='Would you like to view the source code on GitHub?')
        if response == 'yes':
            webbrowser.open(
                'https://github.com/tpauldike/CodeClauseInternship')

    def evaluate(self):
        current_str = self.display.get()
        for char in current_str:
            if char not in '0123456789+-*/^.÷×':
                messagebox.showwarning(
                    title='Invalid Input', message='Your input is not valid')
                self.clear()
                return
        self.last_answer = Caculator().execute(current_str)
        answer = str(self.last_answer)
        if answer and len(answer) > 2:
            if answer[-2] == '.' and answer[-1] == '0':
                self.last_answer = Caculator.clear_dot_zero(
                    self, self.last_answer)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.last_answer)

    def square(self):
        current_str = self.display.get()
        if str(current_str)[-1] in '+-÷×^*/.':
            return
        self.last_answer = Caculator.square_of(self, self.display.get())
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.last_answer)

    def square_root_of(self):
        current_str = self.display.get()
        if current_str == '0':
            messagebox.showinfo(
                title='No Number Entered', message='Enter the number first, whose square root you wish to find')
            return
        for char in current_str:
            if char in '+-÷×^*/' or current_str[-1] == '.':
                messagebox.showerror(
                    title='Invalid Operation', message='Enter a valid number, with no arithmetical symbol')
                return
        self.last_answer = Caculator.square_root_of(self, current_str)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.last_answer)

    def check_valid_char(self, event):
        allowed_chars = set('0123456789+-*/^.÷×')
        self.count = 0
        allowed_keys = ['Shift_L', 'Shift_R' 'Control_L', 'Control_R', 'Alt_L',
                        'Alt_R', 'Tab', 'Caps_Lock', 'Backspace', 'space', 'Return', 'Escape']

        if event.keysym == 'Return':
            self.evaluate()
            return
        elif event.keysym == 'BackSpace':
            self.delete_last_char()
            return
        elif event.keysym == 'Escape':
            self.clear()
        elif event.keysym == 'Alt_R':
            self.show_last_ans()

        if event.char not in allowed_chars and event.keysym not in allowed_keys:
            return
        if event.char in '+-÷×*/':
            self.display_sign(event.char)
        elif event.char in '0123456789':
            self.display_char(event.char)
        elif event.char in '.^':
            self.display_once(event.char)
