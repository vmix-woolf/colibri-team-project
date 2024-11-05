from collections import UserDict


class Address(UserDict):

    def __init__(self, city, street, building, apartment=None):
        super().__init__()
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment