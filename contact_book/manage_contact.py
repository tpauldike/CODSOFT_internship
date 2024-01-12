import sqlite3
from sqlite3 import Error
from datetime import datetime

class Contacts:
    def __init__(self) -> None:
        '''the class responsible for database settings and communication'''
        
    def set_up_database() -> None:
        '''creates the database and table(s), if they don't already exist'''
        try:
            connection = sqlite3.connect('contacts.db')
            cursor = connection.cursor()
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                email TEXT,
                address TEXT,
                created_at NOT NULL,
                updated_at NOT NULL)''')
        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:        
                connection.commit()
                connection.close()
        
    def create_contact(self, name: str, phone: str, email: str, address: str) -> str | None:
        '''creates a new contacts with the details supplied'''
        current_timestamp = datetime.now().strftime('%d/%m/%Y by %H:%M:%S')
        created_at = updated_at = current_timestamp
        
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            
            cursor.execute('INSERT INTO contacts (name, phone, email, address, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)', (name, phone, email, address, created_at, updated_at))
            
            return f'New contact {name} succesfully created'
            
        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:
                connection.commit()
                connection.close()
        
    def update_contact(self, id: int, name: str, phone: str, email: str, address: str) -> str | None:
        '''updates an existing contact'''
        current_timestamp = datetime.now().strftime('%d/%m/%Y by %H:%M:%S')
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            
            if not cursor.execute('SELECT * FROM contacts WHERE id=?', (id,)).fetchone():
                return
            
            cursor.execute('UPDATE contacts SET name=?, phone=?, email=?, address=?, updated_at=? WHERE id=?', (name, phone, email, address, current_timestamp, id))
            
            return f'Contact succesfully updated'
        
        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:
                connection.commit()
                connection.close()
    
    def get_all_contacts(self) -> list | None:
        '''fetches all contacts currently saved in the database'''
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            
            contacts = cursor.execute('SELECT * FROM contacts ORDER BY name ASC').fetchall()
            return contacts
        
        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:
                connection.close()
    
    def get_single_contact(self, name: str) -> tuple | None:
        '''fetches the first contact with the given name, from the database'''
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            
            contact = cursor.execute('SELECT * FROM contacts WHERE name=?', (name,)).fetchone()
            if contact:
                return contact
        
        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:
                connection.close()
    
    def search_contacts(self, given_string: str) -> tuple | None:
        '''returns all contact with the given string in their names'''
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            
            contacts = cursor.execute('SELECT name FROM contacts WHERE name LIKE ?', (f'%{given_string}%',)).fetchall()
            if contacts:
                return contacts

        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:
                connection.close()
                
    def search_by_phone(self, phone: str) -> tuple | None:
        '''returns all contact with the given number in their numbers'''
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            
            contacts = cursor.execute('SELECT name FROM contacts WHERE phone LIKE ?', (f'%{phone}%',)).fetchall()
            if contacts:
                return contacts

        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:
                connection.close()
    
    def delete_contacts(self, names: tuple) -> str | None:
        '''deletes the given contact(s)'''
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            
            placeholders = ', '.join(['?' for _ in names])
            cursor.execute(
                f"DELETE FROM contacts WHERE name IN ({placeholders})", names)
            
            row_count = cursor.rowcount
            connection.commit()
            
            return f'No. of contacts deleted: {row_count}'
        
        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:
                connection.close()

    def email_exists(self, email: str) -> bool:
        '''returns True if a contact with the given email already exists'''
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            
            contact = cursor.execute('SELECT * FROM contacts WHERE email=?', (email,)).fetchone()
            if not contact or contact[3] == '':
                return False
            return True
        
        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:
                connection.close()
                
    def phone_exists(self, phone: str) -> bool | None:
        '''returns True if a contact with the given phone number already exists'''
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            
            if cursor.execute('SELECT * FROM contacts WHERE phone=?', (phone,)).fetchone():
                return True
        
        except Error as e:
            print(f'SQLite Error: {e}')
        finally:
            if connection:
                connection.close()