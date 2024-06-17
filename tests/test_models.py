import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Customer, Table, Reservation

class TestModels(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def test_customer_model(self):
        customer = Customer(name="John Doe", phone="1234567890")
        self.session.add(customer)
        self.session.commit()
        retrieved_customer = self.session.query(Customer).first()
        self.assertEqual(retrieved_customer.name, "John Doe")
        self.assertEqual(retrieved_customer.phone, "1234567890")

    def test_table_model(self):
        table = Table(number=1, capacity=4)
        self.session.add(table)
        self.session.commit()
        retrieved_table = self.session.query(Table).first()
        self.assertEqual(retrieved_table.number, 1)
        self.assertEqual(retrieved_table.capacity, 4)

    def test_reservation_model(self):
        customer = Customer(name="John Doe", phone="1234567890")
        table = Table(number=1, capacity=4)
        self.session.add(customer)
        self.session.add(table)
        self.session.commit()

        reservation = Reservation(customer=customer, table=table, date_time="2023-06-15 19:00")
        self.session.add(reservation)
        self.session.commit()

        retrieved_reservation = self.session.query(Reservation).first()
        self.assertEqual(retrieved_reservation.customer.name, "John Doe")
        self.assertEqual(retrieved_reservation.table.number, 1)
        self.assertEqual(retrieved_reservation.date_time, "2023-06-15 19:00")

if __name__ == '__main__':
    unittest.main()
