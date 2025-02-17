class Reservation:
    def __init__(self, customer, hotel):
        self.customer = customer
        self.hotel = hotel

    def create_reservation(self):
        return self.hotel.reserve_room(self.customer)

    def cancel_reservation(self):
        return self.hotel.cancel_reservation(self.customer)
