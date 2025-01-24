
## Project : Phonebook Application

import pickle

class Phonebook:
    def __init__(self):
        self.contacts = self.load_contacts()


    def load_contacts(self):
        try:
            with open('contacts.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print('No contacts found. Starting with an empty phonebook.')
            return []

    # Save contacts to pickle file
    def save_contacts(self):
        with open('contacts.pkl', 'wb') as file:
            pickle.dump(self.contacts, file)
        print("Contacts saved successfully.")

    # Add contact
    def add_contact(self, name, phone):
        if self.check_duplicate(name, phone):
            print('Contact already exists.')
            return
        self.contacts.append({"name": name, "phone": phone})
        print(f"Contact '{name}' added.")
    
    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone']}")



