import mysql.connector
from contact import Contact
import configparser


class Data:
    def __init__(self):

        appConfig = configparser.ConfigParser()
        appConfig.read('config.ini')
        dbConfig = dict(appConfig.items('Database'))

        self.db = mysql.connector.connect(**dbConfig)

    def getContactById(self, id):
        sql = "SELECT * FROM contacts WHERE id = (%s)"
        values = list()
        values.append(id)
        cursor = self.db.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()
        contact = Contact(*result)
        return contact

    def read(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM contacts"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def insert(self, contact: Contact):
        sql = "INSERT INTO contacts (name, address, phone, email) VALUES (%s, %s, %s, %s)"
        values = (contact.name, contact.address, contact.phone, contact.email)
        cursor = self.db.cursor()
        cursor.execute(sql, values)
        self.db.commit()

    def update(self, contact: Contact):
        sql = "UPDATE contacts SET name = (%s), address = (%s), phone = (%s), email = (%s) WHERE id = (%s)"
        values = (contact.name, contact.address,
                  contact.phone, contact.email, contact.id)
        cursor = self.db.cursor()
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, contact: Contact):
        sql = "DELETE FROM contacts WHERE id = (%s)"
        values = list()
        values.append(contact.id)
        cursor = self.db.cursor()
        cursor.execute(sql, values)
        self.db.commit()
