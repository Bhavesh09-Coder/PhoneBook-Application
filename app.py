
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

    # Search contacts
    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact['name'] or query in contact['phone']]
        if results:
            for contact in results:
                print(f"{contact['name']} - {contact['phone']}")
        else:
            print("No matching contacts found.")

    # Delete contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted.")
                return
        print("Contact not found.")




