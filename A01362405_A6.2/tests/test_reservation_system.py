import unittest
from reservation_system.hotel import Hotel
from reservation_system.customer import Customer
from reservation_system.reservation import Reservation

class TestReservationSystem(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel("Holiday Inn", "New York", 5)
        self.customer = Customer("John Doe", "12345")
        self.reservation = Reservation(self.customer, self.hotel)

    def test_create_reservation(self):
        result = self.reservation.create_reservation()
        self.assertEqual(result, "Room reserved for John Doe.")

    def test_cancel_reservation(self):
        self.reservation.create_reservation()
        result = self.reservation.cancel_reservation()
        self.assertEqual(result, "Reservation for John Doe cancelled.")

    def test_modify_customer_info(self):
        self.customer.modify_info(name="Jane Doe")
        self.assertEqual(self.customer.name, "Jane Doe")

    def test_modify_hotel_info(self):
        self.hotel.modify_info(name="Grand Hotel", rooms=10)
        self.assertEqual(self.hotel.name, "Grand Hotel")
        self.assertEqual(self.hotel.rooms, 10)
