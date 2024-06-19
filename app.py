# app.py

import argparse
from database import Database
from models import Customer, Reservation
from cli import handle_commands

# Initialize database connection
db = Database('restaurant.db')  # Specify the database name here
customer_model = Customer(db)
reservation_model = Reservation(db)

if __name__ == "__main__":
    handle_commands(customer_model, reservation_model)
