from app.database import Database
from app.models import Reservation, Customer, Table
from app.utils import display_reservations, make_reservation, get_available_tables

def main():
    db = Database()
    db.create_tables()

    while True:
        print("Welcome to the Restaurant Reservation System")
        print("1. View Reservations")
        print("2. Make a Reservation")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            display_reservations(db.session)
        elif choice == "2":
            customer = make_reservation(db.session)
            print(f"Reservation made for {customer.name}")
        elif choice == "3":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
