# Phonebook Application

This Python-based Phonebook application allows users to manage their contacts efficiently. It provides options to add, view, search, and delete contacts, along with the ability to save them persistently using a pickle file.

## Features

1. **View Contacts**:
   - Displays all saved contacts with their names and phone numbers.

2. **Add Contact**:
   - Adds a new contact with a name and phone number.
   - Prevents duplicate entries.

3. **Search Contact**:
   - Searches for a contact by name or phone number.
   - Displays all matching results.

4. **Delete Contact**:
   - Deletes a contact by name.

5. **Save & Exit**:
   - Saves all contacts to a pickle file (`contacts.pkl`) and exits the application.

## Requirements

- Python 3.x

## How to Use

1. Clone or download the script.
2. Run the script:
   ```bash
   python phonebook.py
   ```
3. Follow the menu options:
   - `1`: View all saved contacts.
   - `2`: Add a new contact by providing a name and phone number.
   - `3`: Search for a contact by name or phone number.
   - `4`: Delete an existing contact by name.
   - `5`: Save the contacts and exit the application.

## Persistent Storage

- Contacts are stored in a file named `contacts.pkl` using Python's `pickle` module.
- The file is automatically created if it does not exist.
- Contacts are automatically loaded when the application starts.

## Example Usage

### Adding a Contact
```
Enter contact name: John Doe
Enter contact phone number: 1234567890
Contact 'John Doe' added.
```

### Viewing Contacts
```
1. John Doe - 1234567890
```

### Searching Contacts
```
Enter search query: John
John Doe - 1234567890
```

### Deleting a Contact
```
Enter contact name to delete: John Doe
Contact 'John Doe' deleted.
```

## Code Structure

- **Phonebook Class**:
  - Handles all phonebook operations (add, view, search, delete, save, and load contacts).

- **Main Function**:
  - Provides a user-friendly menu to interact with the Phonebook class.

## Future Enhancements

- Add support for editing existing contacts.
- Improve search functionality (e.g., case-insensitive or partial matches).
- Implement a graphical user interface (GUI).

---

