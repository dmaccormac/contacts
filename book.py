import pandas as pd
from contact import Contact
from database import Database


class Book:
    def __init__(self):
        self.db = Database()

    def view(self):
        contacts = self.db.getAll()
        results = list()
        for contact in contacts:
            results.append((*contact,))

        table = self._formatTable(results)
        return (table)

    def add(self, name, address, phone, email):
        contact = Contact(None, name, address, phone, email)
        self.db.insert(contact)

    def update(self, id):
        contact = self.db.get(id)
        updated_contact = self._updateContact(contact)
        self.db.update(updated_contact)

    def delete(self, id):
        self.db.delete(id)

    def search(self, term):
        results = self.db.search(term)
        return self._formatTable(results)

    def _formatTable(self, contacts: list):
        dataFrame = pd.DataFrame(
            contacts, columns=['Id', 'Name', 'Address', 'Phone', 'Email'])
        dataFrame.set_index('Id', inplace=True)

        return (dataFrame)

    def _updateContact(self, contact: Contact):
        update_list = list()
        record = (*contact,)

        for field in range(1, len(record)):
            value = input('[' + record[field] + ']:')
            if (value != ''):
                update_list.append(value)
            else:
                update_list.append(record[field])

        return Contact(contact.id, *update_list)
