import pandas as pd
from contact import Contact
from data import Data


class Book:
    def __init__(self):
        self.contacts = list()
        self.db = Data()

    def createTable(self, contacts: list):
        df = pd.DataFrame(
            contacts, columns=['Id', 'Name', 'Address', 'Phone', 'Email'])
        df.set_index('Id', inplace=True)

        return (df)

    def view(self):
        self.contacts.clear()

        items = self.db.read()
        for item in items:
            self.contacts.append(Contact(*item))

        results = list()
        for contact in self.contacts:
            results.append((*contact,))

        table = self.createTable(self.contacts)
        return (table)

    def add(self, name, address, phone, email):
        contact = Contact(None, name, address, phone, email)
        self.db.insert(contact)

    def update(self, id, name, address, phone, email):
        contact = Contact(id, name, address, phone, email)
        self.db.update(contact)

    def delete(self, id):
        contact = Contact(id, None, None, None, None)
        self.db.delete(contact)
