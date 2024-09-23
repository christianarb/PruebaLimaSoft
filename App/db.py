# db.py
from config import DB_CONFIG
from config import SQL_QUERY_PERSONAS
import mysql.connector

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = mysql.connector.connect(**DB_CONFIG)
        return self.connection

    def get_personas(self):
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY_PERSONAS)
        personas = cursor.fetchall()
        cursor.close()
        return personas

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
