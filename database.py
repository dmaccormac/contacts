import mysql.connector
from contact import Contact


class Database:
    def __init__(self, dbConfig):
        self.dbConfig = dbConfig
        self.db = None
        self.cursor = None

    def openDatabase(self, name):
        try:
            self.db = mysql.connector.connect(**self.dbConfig, database=name)
        except:
            print("could not open database")

    def createDatabase(self, name):
        # connect to server
        try:
            self.db = mysql.connector.connect(**self.dbConfig)

        except:
            print("could not connect to database server")

        # create the database
        try:
            cursor = self.db.cursor()
            sql = f"CREATE DATABASE {name}"
            cursor.execute(sql)
        except:
            print("could not create database")

        # connect to database and create table
        try:
            self.db = mysql.connector.connect(**self.dbConfig, database=name)
            sql = """CREATE TABLE contacts
                    (id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    address VARCHAR(255),
                    phone VARCHAR(255),
                    email VARCHAR(255))"""
            cursor = self.db.cursor()
            cursor.execute(sql)
        except:
            print("could not create table")

    def getLimit(self, offset, maxRows):
        cursor = self.db.cursor()
        sql = f"SELECT * FROM contacts ORDER BY id LIMIT {offset},{maxRows}"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

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
