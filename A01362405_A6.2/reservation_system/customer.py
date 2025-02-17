class Customer:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def create_customer(self):
        pass

    def delete_customer(self):
        pass

    def display_info(self):
        return f"Customer {self.name} with ID {self.id_number}."

    def modify_info(self, name=None, id_number=None):
        if name:
            self.name = name
        if id_number:
            self.id_number = id_number
