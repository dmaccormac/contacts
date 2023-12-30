import mysql.connector
import pandas as pd
from dbconf import *


class ContactBook:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def read(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM people"
        cursor.execute(sql)
        results = cursor.fetchall()
        results.sort()

        df = pd.DataFrame(results, columns=[
                          'Id', 'Firstname', 'Lastname', 'Phone', 'Email'])
        df.set_index('Id', inplace=True)
        return (df)
