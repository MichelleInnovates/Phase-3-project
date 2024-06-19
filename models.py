import sqlite3

class Database:
    def __init__(self, db_name="restaurant.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

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

class Customer:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def create(self, name, phone=None):
        query = "INSERT INTO customers (name, phone) VALUES (?, ?)"
        self.db_conn.execute_query(query, (name, phone))

    def get_all(self):
        query = "SELECT * FROM customers"
        return self.db_conn.fetch_query(query)

class Reservation:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def create(self, customer_id, date, time, num_guests):
        query = "INSERT INTO reservations (customer_id, date, time, num_guests) VALUES (?, ?, ?, ?)"
        self.db_conn.execute_query(query, (customer_id, date, time, num_guests))

    def get_all(self):
        query = "SELECT * FROM reservations"
        return self.db_conn.fetch_query(query)