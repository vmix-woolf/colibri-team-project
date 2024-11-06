from collections import UserDict


class Address(UserDict):

    def __init__(self, city, street, building, apartment):
        super().__init__()
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment