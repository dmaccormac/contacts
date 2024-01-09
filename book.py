import pandas as pd
import configparser
from contact import Contact
from database import Database


class Book:
    def __init__(self):
        appConfig = configparser.ConfigParser()
        appConfig.read('config.ini')
        dbConfig = dict(appConfig.items('Database'))
        self.db = Database(dbConfig)

    def open(self, name):
        self.db.openDatabase(name)

    def create(self, name):
        self.db.createDatabase(name)

    def view(self):
        contacts = self.db.getAll()
        results = list()
        for contact in contacts:
            results.append((*contact,))

        table = self._formatTable(results)
        return (table)

    def viewPages(self):
        offset = 0
        maxRows = 10

        while True:
            contacts = self.db.getLimit(offset, maxRows)
            if (contacts == []):
                break

            self._clearScreen()
            print(self._formatTable(contacts))
            input(":")
            offset += maxRows

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
        field_names = ["Id", "Name", "Address", "Phone", "Email"]

        for field in range(1, len(record)):
            prompt = record[field] if record[field] else "None"
            value = input(field_names[field] + " [" + prompt + "]:")
            if (value != ''):
                update_list.append(value)
            else:
                update_list.append(record[field])

        return Contact(contact.id, *update_list)

    def _clearScreen(self):
        print("\033c", end='')
