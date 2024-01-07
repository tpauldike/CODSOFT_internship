import tkinter as tk


class GUI:

    def __init__(self) -> None:
        '''Builds the GUI of the contact list app'''
        # Main colors
        self.root_bg = '#023949'
        self.root_bg2 = '#222222'
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

        self.root = tk.Tk()
        self.root.title('Contact Manager')
        self.centralize_window(self.root, 900, 600)
        self.root.config(bg=self.root_bg)

        self.display_home_page()

        self.root.mainloop()

    def centralize_window(self, window: object, width: int, height: int):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{str(width)}x{str(height)}+{x}+{y}")

    def display_home_page(self):
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

    def display_input_fields(self, labeltext: str):
        self.destroy_all_widgets()
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
            self.input_fields_btn_cont, text='save', cnf=self.save_btn_cnf)
        self.save_btn.grid(row=0, column=1)

    def back_home(self):
        self.destroy_all_widgets()
        self.display_home_page()
        self.root.config(bg=self.root_bg)

    def destroy_all_widgets(self):
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

    def display_contacts(self):
        self.destroy_all_widgets()
        self.contact_management_frame = tk.Frame(
            self.root, bg=self.root_bg, padx=10)
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
            self.management_btn_cont, text='delete', cnf=self.management_btn_cnf, width=5)
        self.management_delete_btn.grid(row=0, column=3)

        self.management_add_new_btn = tk.Button(self.management_btn_cont, text='add new', cnf=self.management_btn_cnf,
                                                width=6, command=lambda: self.display_input_fields('Add New Contact'))
        self.management_add_new_btn.grid(row=0, column=4)

    def display_contact_details(self):
        if hasattr(self, 'contact_details') and self.contact_details.winfo_exists():
            self.close_contact_details()
            return
        
        self.contact_details = tk.LabelFrame(self.root, bg=self.contact_details_bg, padx=10, pady=50)
        self.contact_details.place(x=230, y=150)
        
        self.contact_name_label = tk.Label(
            self.contact_details, text='Name: ', cnf=self.contact_label_cnf)
        self.contact_name_label.grid(row=0, column=0)
        self.contact_name_displayed = tk.Entry(
            self.contact_details, cnf=self.details_displayed)
        self.contact_name_displayed.grid(row=0, column=1)

        self.contact_phone_label = tk.Label(
            self.contact_details, text='Phone: ', cnf=self.contact_label_cnf)
        self.contact_phone_label.grid(row=1, column=0)
        self.contact_phone_displayed = tk.Entry(
            self.contact_details, cnf=self.details_displayed)
        self.contact_phone_displayed.grid(row=1, column=1)

        self.contact_email_label = tk.Label(
            self.contact_details, text='Email: ', cnf=self.contact_label_cnf)
        self.contact_email_label.grid(row=2, column=0)
        self.contact_email_displayed = tk.Entry(
            self.contact_details, cnf=self.details_displayed)
        self.contact_email_displayed.grid(row=2, column=1)

        self.contact_email_label = tk.Label(
            self.contact_details, text='Address: ', cnf=self.contact_label_cnf)
        self.contact_email_label.grid(row=3, column=0)
        self.contact_email_displayed = tk.Text(
            self.contact_details, cnf={'font': ('Gerogia', 13), 'state': 'disabled', 'width': 30, 'bg': self.input_bg}, height=3, pady=5)
        self.contact_email_displayed.grid(row=3, column=1, rowspan=4)
        
        self.close_btn = tk.Button(
            self.contact_details, text='close', cnf=self.search_btn_cnf, command=self.close_contact_details)
        self.close_btn.place(x=300, y=182)
        
        self.root.config(bg=self.root_bg2)
        self.contact_management_frame.config(bg=self.root_bg2)
        
    def close_contact_details(self):
        self.root.config(bg=self.root_bg)
        self.contact_management_frame.config(bg=self.root_bg)
        self.contact_details.destroy()
        
    def search_contact(self):
        if hasattr(self, 'contact_details') and self.contact_details.winfo_exists():
            self.close_contact_details()
    
 # '#234346'
