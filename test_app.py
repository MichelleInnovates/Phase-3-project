import unittest
import sqlite3
from database import Database
from models import Customer, Reservation

# Initialize a temporary database for testing
TEST_DB = 'test.db'

class TestCustomerModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Connect to the temporary test database
        cls.db = Database(TEST_DB)
        cls.customer_model = Customer(cls.db)

    def setUp(self):
        # Reset tables before each test
        self.db.execute_query("DELETE FROM customers")
        self.db.execute_query("DELETE FROM reservations")

    def test_create_customer(self):
        # Test creating a new customer
        self.customer_model.create("John Doe", "1234567890")

        # Verify if customer exists in the database
        result = self.db.fetch_query("SELECT * FROM customers WHERE name=?", ("John Doe",))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][2], "1234567890")  # Phone number should match

    def test_list_customers(self):
        # Test listing all customers
        self.customer_model.create("Jane Smith", "9876543210")

        customers = self.customer_model.get_all()
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0][1], "Jane Smith")  # Check if customer name matches

    def tearDown(self):
        # Clean up after each test
        self.db.execute_query("DELETE FROM customers")
        self.db.execute_query("DELETE FROM reservations")

    @classmethod
    def tearDownClass(cls):
        # Close database connection after all tests
        del cls.customer_model
        del cls.db
        conn = sqlite3.connect(TEST_DB)
        conn.execute("DROP TABLE IF EXISTS customers")
        conn.execute("DROP TABLE IF EXISTS reservations")
        conn.close()


class TestReservationModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Connect to the temporary test database
        cls.db = Database(TEST_DB)
        cls.reservation_model = Reservation(cls.db)
        cls.customer_model = Customer(cls.db)

    def setUp(self):
        # Reset tables before each test
        self.db.execute_query("DELETE FROM customers")
        self.db.execute_query("DELETE FROM reservations")
        self.customer_model.create("John Doe", "1234567890")
        self.customer_id = self.db.fetch_query("SELECT id FROM customers WHERE name=?", ("John Doe",))[0][0]

    def test_create_reservation(self):
        # Test creating a new reservation
        self.reservation_model.create(self.customer_id, "2024-06-21", "19:00", 4)

        # Verify if reservation exists in the database
        result = self.db.fetch_query("SELECT * FROM reservations WHERE customer_id=?", (self.customer_id,))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][3], "19:00")  # Time should match

    def test_list_reservations(self):
        # Test listing all reservations
        self.reservation_model.create(self.customer_id, "2024-06-21", "19:00", 4)

        reservations = self.reservation_model.get_all()
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0][2], "2024-06-21")  # Check if date matches

    def tearDown(self):
        # Clean up after each test
        self.db.execute_query("DELETE FROM customers")
        self.db.execute_query("DELETE FROM reservations")

    @classmethod
    def tearDownClass(cls):
        # Close database connection after all tests
        del cls.reservation_model
        del cls.customer_model
        del cls.db
        conn = sqlite3.connect(TEST_DB)
        conn.execute("DROP TABLE IF EXISTS customers")
        conn.execute("DROP TABLE IF EXISTS reservations")
        conn.close()

if __name__ == '__main__':
    unittest.main()

