import argparse
from models import Customer, Reservation

def handle_commands(customer_model, reservation_model):
    parser = argparse.ArgumentParser(description="Restaurant Reservation CLI")

    parser.add_argument("--create-customer", action="store_true", help="Create a new customer")
    parser.add_argument("--list-customers", action="store_true", help="List all customers")

    parser.add_argument("--create-reservation", action="store_true", help="Create a new reservation")
    parser.add_argument("--list-reservations", action="store_true", help="List all reservations")

    args = parser.parse_args()

    # Handle commands using customer_model and reservation_model
    if args.create_customer:
        name = input("Enter customer name: ")
        phone = input("Enter customer phone (optional): ")
        customer_model.create(name, phone)
        print("Customer created successfully.")

    elif args.list_customers:
        customers = customer_model.get_all()
        if customers:
            print("List of customers:")
            for customer in customers:
                print(customer)
        else:
            print("No customers found.")

    elif args.create_reservation:
        customer_id = int(input("Enter customer ID: "))
        date = input("Enter reservation date (YYYY-MM-DD): ")
        time = input("Enter reservation time: ")
        num_guests = int(input("Enter number of guests: "))
        reservation_model.create(customer_id, date, time, num_guests)
        print("Reservation created successfully.")

    elif args.list_reservations:
        reservations = reservation_model.get_all()
        if reservations:
            print("List of reservations:")
            for reservation in reservations:
                print(reservation)
        else:
            print("No reservations found.")

if __name__ == "__main__":
    # Initialize models and handle commands
    customer_model = Customer()
    reservation_model = Reservation()
    handle_commands(customer_model, reservation_model)