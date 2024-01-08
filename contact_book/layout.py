import tkinter as tk
from manage_contact import Contacts
from tkinter import messagebox

class GUI:

    def __init__(self) -> None:
        '''Builds the GUI of the contact list app'''
        # Main colors
        self.root_bg = '#023949'
        self.fade_color = '#222222'
        self.focus_color = '#101010'
        self.error_color = '#888844'
        self.text_color = '#FFFFFF'
        self.input_bg = '#AFEFE9'
        self.highlight_bg = '#022939'
        self.contact_details_bg = '#124856'

        # Common configurations
        self.home_btn_cnf = {'height': 1, 'width': 30, 'relief': 'sunken', 'font': (
            'Verdana', 12, 'bold'), 'bg': '#387f52', 'fg': self.text_color, 'activebackground': '#387f30', 'activeforeground': '#DDDDDD'}

        self.label_field_cnf = {'font': (
            'Gerogia', 12, 'bold'), 'pady': 5, 'justify': 'left', 'bg': self.root_bg, 'fg': self.text_color}

        self.input_fields_cnf = {'font': (
            'Gerogia', 13), 'width': 30, 'highlightthickness': 0, 'bg': self.input_bg}

        self.save_btn_cnf = {'width': 15, 'font': ('Vernada', 11, 'italic'), 'bg': self.root_bg, 'fg': self.text_color,
                             'border': 0, 'activebackground': self.highlight_bg, 'activeforeground': self.text_color, 'relief': 'flat'}

        self.management_btn_cnf = {'bg': self.highlight_bg, 'activebackground': self.root_bg, 'borderwidth': 0,
                                   'fg': self.text_color, 'relief': 'flat', 'activeforeground': self.text_color, 'font': ('Vernada', 11, 'italic')}

        self.search_btn_cnf = {'bg': self.root_bg, 'activebackground': self.highlight_bg, 'borderwidth': 0, 'fg': self.text_color,
                               'relief': 'flat', 'activeforeground': self.text_color, 'font': ('Vernada', 11, 'italic'), 'width': 11}

        self.contact_label_cnf = {'font': (
            'Gerogia', 12, 'bold'), 'pady': 5, 'justify': 'left', 'bg': self.contact_details_bg, 'fg': self.text_color}

        self.details_displayed = {'font': (
            'Gerogia', 13), 'state': 'readonly', 'width': 30, 'readonlybackground': self.input_bg}

        self.date_cnf = {'font': (
            'Gerogia', 10), 'pady': 5, 'justify': 'left', 'bg': self.contact_details_bg, 'fg': self.text_color}
        
        self.root = tk.Tk()
        self.root.title('Contact Manager')
        self.centralize_window(self.root, 900, 600)
        self.root.config(bg=self.root_bg)

        self.display_home_page()
        Contacts.set_up_database()

        self.root.mainloop()

    def centralize_window(self, window: object, width: int, height: int) -> None:
        '''gets the main window centralized on the computer screen'''
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{str(width)}x{str(height)}+{x}+{y}")

    def display_home_page(self) -> None:
        '''creates all widgets present in the home page'''
        self.title = tk.Label(self.root, text='Contact Manager', bg=self.root_bg,
                              fg=self.text_color, font=('Georgia', 25, 'bold'))
        self.title.pack(pady=40, anchor='center')

        self.home = tk.Label(self.root, bg=self.root_bg)
        self.home.pack(anchor='center', pady=90, fill='y')

        self.new_btn = tk.Button(self.home, text='N e w   C o n t a c t', cnf=self.home_btn_cnf,
                                 command=lambda: self.display_input_fields('Add New Contact'))
        self.new_btn.pack(pady=5)
        self.view_btn = tk.Button(self.home, text='V i e w   C o n t a c t s',
                                  cnf=self.home_btn_cnf, command=self.display_contacts)
        self.view_btn.pack(pady=5)
        self.search_btn = tk.Button(
            self.home, text='S e a r c h', cnf=self.home_btn_cnf, command=self.display_contacts)
        self.search_btn.pack(pady=5)
        self.edit_btn = tk.Button(
            self.home, text='E d i t', cnf=self.home_btn_cnf, command=self.display_contacts)
        self.edit_btn.pack(pady=5)
        self.delete_btn = tk.Button(
            self.home, text='D e l e t e', cnf=self.home_btn_cnf, command=self.display_contacts)
        self.delete_btn.pack(pady=5)

    def display_input_fields(self, labeltext: str) -> None:
        '''creates the input fields for adding or updating contacts'''
        self.destroy_all_widgets()
        self.root.config(bg=self.root_bg)
        self.input_fields = tk.LabelFrame(self.root, text=labeltext, font=(
            'Verdana', 14), border=2, pady=15, padx=10, bg=self.root_bg, fg=self.text_color, labelanchor='n')
        self.input_fields.pack(anchor='center', pady=150)

        self.name_label = tk.Label(
            self.input_fields, text='Name: ', cnf=self.label_field_cnf)
        self.name_label.grid(row=0, column=0)
        self.name_input = tk.Entry(
            self.input_fields, cnf=self.input_fields_cnf)
        self.name_input.grid(row=0, column=1)

        self.phone_label = tk.Label(
            self.input_fields, text='Phone: ', cnf=self.label_field_cnf)
        self.phone_label.grid(row=1, column=0)
        self.phone_input = tk.Entry(
            self.input_fields, cnf=self.input_fields_cnf)
        self.phone_input.grid(row=1, column=1)

        self.email_label = tk.Label(
            self.input_fields, text='Email: ', cnf=self.label_field_cnf)
        self.email_label.grid(row=2, column=0)
        self.email_input = tk.Entry(
            self.input_fields, cnf=self.input_fields_cnf)
        self.email_input.grid(row=2, column=1)

        self.address_label = tk.Label(
            self.input_fields, text='Address: ', cnf=self.label_field_cnf)
        self.address_label.grid(row=3, column=0)
        self.address_input = tk.Text(
            self.input_fields, cnf=self.input_fields_cnf, height=3, pady=5)
        self.address_input.grid(row=3, column=1, rowspan=3)

        self.space = tk.Label(self.input_fields, bg=self.root_bg)
        self.space.grid(row=6, column=0, columnspan=2)
        self.input_fields_btn_cont = tk.Label(
            self.input_fields, bg=self.root_bg, pady=10)
        self.input_fields_btn_cont.grid(row=7, column=1)
        self.home_btn = tk.Button(
            self.input_fields_btn_cont, text='back home', cnf=self.save_btn_cnf, command=self.back_home)
        self.home_btn.grid(row=0, column=0)
        self.save_btn = tk.Button(
            self.input_fields_btn_cont, text='save', cnf=self.save_btn_cnf, command=self.save)
        self.save_btn.grid(row=0, column=1)

    def back_home(self) -> None:
        '''destroys all widgets and recreate the home page widgets'''
        self.destroy_all_widgets()
        self.display_home_page()
        self.root.config(bg=self.root_bg)

    def destroy_all_widgets(self) -> None:
        '''checks for certain attributes and destroys them if present'''
        if hasattr(self, 'title') and self.title.winfo_exists():
            self.title.destroy()
        if hasattr(self, 'home') and self.home.winfo_exists():
            self.home.destroy()
        if hasattr(self, 'input_fields') and self.input_fields.winfo_exists():
            self.input_fields.destroy()
        if hasattr(self, 'contact_management_frame') and self.contact_management_frame.winfo_exists():
            self.contact_management_frame.destroy()
        if hasattr(self, 'contact_details') and self.contact_details.winfo_exists():
            self.contact_details.destroy()

    def display_contacts(self) -> None:
        '''displays a list of all the contacts saved'''
        self.destroy_all_widgets()
        self.root.config(bg=self.fade_color)
        
        self.contact_management_frame = tk.Frame(
            self.root, bg=self.fade_color, padx=10)
        self.contact_management_frame.pack(pady=50)

        # Search bar container
        self.search_bar = tk.Frame(
            self.contact_management_frame, bg=self.input_bg)
        self.search_bar.pack(fill='x')

        self.search_input = tk.Entry(self.search_bar, font=(
            'Gerogia', 12), width=20, bg=self.input_bg, highlightthickness=0, borderwidth=5)
        self.search_input.grid(row=0, column=0)

        self.management_search_btn = tk.Button(
            self.search_bar, text='search', cnf=self.search_btn_cnf)
        self.management_search_btn.grid(row=0, column=1)

        # Contact list
        self.contact_list = tk.Listbox(self.contact_management_frame, highlightthickness=0,
                                       borderwidth=10, relief='flat', height=20, bg='#4F8FFF', font=('Vernada', 12))
        self.contact_list.pack(fill='both')

        # Button container
        self.management_btn_cont = tk.Frame(
            self.contact_management_frame, bg=self.root_bg)
        self.management_btn_cont.pack(pady=5)

        self.management_back_btn = tk.Button(
            self.management_btn_cont, text='back', cnf=self.management_btn_cnf, width=4, command=self.back_home)
        self.management_back_btn.grid(row=0, column=0)

        self.management_details_btn = tk.Button(
            self.management_btn_cont, text='details', cnf=self.management_btn_cnf, width=4, command=self.display_contact_details)
        self.management_details_btn.grid(row=0, column=1)

        self.management_edit_btn = tk.Button(self.management_btn_cont, text='edit', cnf=self.management_btn_cnf,
                                             width=4, command=lambda: self.display_input_fields('Update Contact Information'))
        self.management_edit_btn.grid(row=0, column=2)

        self.management_delete_btn = tk.Button(
            self.management_btn_cont, text='delete', cnf=self.management_btn_cnf, width=5, command=self.delete_contacts)
        self.management_delete_btn.grid(row=0, column=3)

        self.management_add_new_btn = tk.Button(self.management_btn_cont, text='add new', cnf=self.management_btn_cnf,
                                                width=6, command=lambda: self.display_input_fields('Add New Contact'))
        self.management_add_new_btn.grid(row=0, column=4)

    def display_contact_details(self) -> None:
        '''displays full details of the selected contact'''
        if hasattr(self, 'contact_details') and self.contact_details.winfo_exists():
            self.close_contact_details()
            return

        self.contact_details = tk.LabelFrame(
            self.root, bg=self.contact_details_bg, padx=10, pady=10)
        self.contact_details.place(x=230, y=120)

        self.contact_date_label = tk.Label(
            self.contact_details, cnf=self.contact_label_cnf)
        self.contact_date_label.grid(row=0, column=0, columnspan=2)
        
        self.date_created = tk.Label(
            self.contact_date_label, text='Date Created: ', cnf=self.date_cnf)
        self.date_created.pack(fill='x', anchor='w')
        
        self.date_created = tk.Label(
            self.contact_date_label, text='Last Modified: ', cnf=self.date_cnf)
        self.date_created.pack(fill='x', anchor='w')
        
        self.contact_name_label = tk.Label(
            self.contact_details, text='Name: ', cnf=self.contact_label_cnf)
        self.contact_name_label.grid(row=1, column=0)
        self.contact_name_displayed = tk.Entry(
            self.contact_details, cnf=self.details_displayed)
        self.contact_name_displayed.grid(row=1, column=1)

        self.contact_phone_label = tk.Label(
            self.contact_details, text='Phone: ', cnf=self.contact_label_cnf)
        self.contact_phone_label.grid(row=2, column=0)
        self.contact_phone_displayed = tk.Entry(
            self.contact_details, cnf=self.details_displayed)
        self.contact_phone_displayed.grid(row=2, column=1)

        self.contact_email_label = tk.Label(
            self.contact_details, text='Email: ', cnf=self.contact_label_cnf)
        self.contact_email_label.grid(row=3, column=0)
        self.contact_email_displayed = tk.Entry(
            self.contact_details, cnf=self.details_displayed)
        self.contact_email_displayed.grid(row=3, column=1)

        self.contact_email_label = tk.Label(
            self.contact_details, text='Address: ', cnf=self.contact_label_cnf)
        self.contact_email_label.grid(row=4, column=0)
        self.contact_email_displayed = tk.Text(
            self.contact_details, cnf={'font': ('Gerogia', 13), 'state': 'disabled', 'width': 30, 'bg': self.input_bg}, height=4, pady=5)
        self.contact_email_displayed.grid(row=4, column=1, rowspan=4)
        
        self.space_before_btn = tk.Label(
            self.contact_details, cnf=self.contact_label_cnf, height=2)
        self.space_before_btn.grid(row=8, column=0, columnspan=2)

        self.close_btn = tk.Button(
            self.contact_details, text='close', cnf=self.search_btn_cnf, command=self.close_contact_details)
        self.close_btn.place(x=300, y=272)

        self.root.config(bg=self.focus_color)
        self.contact_management_frame.config(bg=self.focus_color)

    def close_contact_details(self) -> None:
        '''destroys the contact details parent widget'''
        self.root.config(bg=self.fade_color)
        self.contact_management_frame.config(bg=self.fade_color)
        self.contact_details.destroy()

    def search_contact(self) -> None:
        '''finds all the contacts that have the given string inputed'''
        if hasattr(self, 'contact_details') and self.contact_details.winfo_exists():
            self.close_contact_details()

    def display_error(self, message: str, error_bg='#000000') -> None:
        """toggles the background color and displays the error"""
        self.root.config(bg=error_bg)
        messagebox.showerror(title='Error', message=message)
        self.root.config(bg=self.root_bg)
        
    def delete_contacts(self) -> None:
        '''deletes the currently selected contact(s)'''
        pass
        
    def save(self) -> None:
        self.display_error('This function has not been implemented yet, try again later')
        
 # '#234346'
