import mysql.connector
from dbconf import *
from contact import Contact


class Data:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

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

    def update(self, contact):
        sql = "UPDATE contacts SET name = (%s), address = (%s), phone = (%s), email = (%s) WHERE id = (%s)"
        values = (contact.name, contact.address,
                  contact.phone, contact.email, contact.id)
        cursor = self.db.cursor()
        cursor.execute(sql, values)
        self.db.commit()
