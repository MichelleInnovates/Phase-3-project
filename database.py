# database.py

import sqlite3

class Database:
    def __init__(self, db_name="restaurant.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()  # Add this line to execute schema.sql

    def create_tables(self):
        with open('schema.sql', 'r') as f:
            schema = f.read()
            self.cursor.executescript(schema)
        self.conn.commit()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def fetch_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
