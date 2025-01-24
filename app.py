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

    # Check for duplicate contacts
    def check_duplicate(self, name, phone):
        for contact in self.contacts:
            if contact['name'] == name and contact['phone'] == phone:
                return True
        return False

def main():
    phonebook = Phonebook()
    while True:
        print("\nPhonebook Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save & Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            phonebook.view_contacts()
        elif choice == '2':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            phonebook.add_contact(name, phone)
        elif choice == '3':
            query = input("Enter search query: ")
            phonebook.search_contact(query)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            phonebook.delete_contact(name)
        elif choice == '5':
            phonebook.save_contacts()
            print("Exiting phonebook.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()