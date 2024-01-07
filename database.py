import mysql.connector
from contact import Contact
import configparser


class Database:
    def __init__(self):
        appConfig = configparser.ConfigParser()
        appConfig.read('config.ini')
        dbConfig = dict(appConfig.items('Database'))

        self.db = mysql.connector.connect(**dbConfig)

    def get(self, id):
        sql = "SELECT * FROM contacts WHERE id = (%s)"
        values = list()
        values.append(id)
        cursor = self.db.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()
        contact = Contact(*result)
        return contact

    def getAll(self):
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

    def delete(self, id):
        sql = "DELETE FROM contacts WHERE id = (%s)"
        values = list()
        values.append(id)
        cursor = self.db.cursor()
        cursor.execute(sql, values)
        self.db.commit()

    def search(self, term):
        term = f"%{term}%"
        cursor = self.db.cursor()
        sql = "SELECT * FROM contacts WHERE name LIKE (%s)"
        values = list()
        values.append(term)
        cursor.execute(sql, values)
        results = cursor.fetchall()
        return (results)
