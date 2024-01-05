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

    def update(self, id):
        contact = self.db.getContactById(id)
        updated_contact = self.getUpdateValues(contact)
        self.db.update(updated_contact)

    def getUpdateValues(self, contact: Contact):
        update_list = list()
        record = (*contact,)

        for field in range(1, len(record)):
            value = input('[' + record[field] + ']:')
            if (value != ''):
                update_list.append(value)
            else:
                update_list.append(record[field])

        return Contact(contact.id, *update_list)

    def delete(self, id):
        contact = Contact(id, None, None, None, None)
        self.db.delete(contact)
