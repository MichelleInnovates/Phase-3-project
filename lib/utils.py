from .models import Reservation, Customer, Table

def display_reservations(session):
    reservations = session.query(Reservation).all()
    for reservation in reservations:
        print(reservation)

def make_reservation(session):
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    date_time = input("Enter the reservation date and time (YYYY-MM-DD HH:MM): ")

    customer = session.query(Customer).filter_by(name=name, phone=phone).first()
    if not customer:
        customer = Customer(name=name, phone=phone)
        session.add(customer)
        session.commit()

    available_tables = get_available_tables(session, date_time)
    if available_tables:
        table = available_tables[0]
        reservation = Reservation(customer=customer, table=table, date_time=date_time)
        session.add(reservation)
        session.commit()
        return customer
    else:
        print("Sorry, no available tables for the requested date and time.")
        return None

def get_available_tables(session, date_time):
    reserved_tables = session.query(Reservation.table_id).filter_by(date_time=date_time).all()
    reserved_table_ids = [table_id for table_id, in reserved_tables]
    available_tables = session.query(Table).filter(~Table.id.in_(reserved_table_ids)).all()
    return available_tables
