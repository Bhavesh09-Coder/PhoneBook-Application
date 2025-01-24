
## Project : Phonebook Application

import pickle

class Phonebook:
    def __init__(self):
        self.contacts = self.load_contacts()