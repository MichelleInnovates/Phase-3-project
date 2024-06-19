##Restaurant Reservation CLI Application
This command-line interface (CLI) application allows users to manage customer information and reservations for a restaurant. It uses SQLite for database storage and provides basic CRUD operations through a simple ORM (Object-Relational Mapping) implemented in Python.

##Features
Create Customer: Add new customers to the database with optional phone number.
List Customers: View a list of all customers stored in the database.
Create Reservation: Make reservations for customers, specifying date, time, and number of guests.
List Reservations: Display a list of all reservations made.

#Installation
Clone the Repository:
git clone <https://github.com/MichelleInnovates/Phase-3-project>


##Database Initialization:

Ensure Python 3.x and SQLite are installed.
Execute the schema.sql file to create the SQLite database and tables:
sqlite3 restaurant.db < schema.sql

##Usage
Run the CLI application by executing app.py with Python:
python3 app.py --create-customer John Doe 1234567890
python3 app.py --list-customers
python3 app.py --create-reservation 1 2024-06-20 18:00 4
python3 app.py --list-reservations


##Command-Line Arguments
--create-customer: Create a new customer with a name and optional phone number.
--list-customers: Display a list of all customers.
--create-reservation: Make a reservation by providing customer ID, date, time, and number of guests.
--list-reservations: Show a list of all reservations.

##Project Structure
app.py: Main script to handle CLI commands and interact with the database.
database.py: Contains the Database class to manage SQLite database connection and operations.
models.py: Defines ORM classes (Customer and Reservation) for interacting with database tables.
cli.py: Implements command-line argument parsing and command handling functions.
schema.sql: SQL schema file defining database tables (customers and reservations).

##Contributing
Contributions are welcome! Fork the repository and submit a pull request with your improvements or bug fixes.

