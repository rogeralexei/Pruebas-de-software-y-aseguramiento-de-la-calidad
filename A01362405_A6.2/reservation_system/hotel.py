class Hotel:
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def create_hotel(self):
        pass

    def delete_hotel(self):
        pass

    def display_info(self):
        return f"Hotel {self.name} located in {self.location}, with {self.rooms} rooms."

    def modify_info(self, name=None, location=None, rooms=None):
        if name:
            self.name = name
        if location:
            self.location = location
        if rooms:
            self.rooms = rooms

    def reserve_room(self, customer):
        if self.rooms > 0:
            self.reservations.append(customer)
            self.rooms -= 1
            return f"Room reserved for {customer.name}."
        return "No rooms available."

    def cancel_reservation(self, customer):
        if customer in self.reservations:
            self.reservations.remove(customer)
            self.rooms += 1
            return f"Reservation for {customer.name} cancelled."
        return "Reservation not found."
