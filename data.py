import mysql.connector
from dbconf import *


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
