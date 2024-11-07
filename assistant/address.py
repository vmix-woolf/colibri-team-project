from collections import UserDict

class Address(UserDict):
    def __init__(self, city, street, building, apartment):
        super().__init__()
        self['city'] = city
        self['street'] = street
        self['building'] = building
        self['apartment'] = apartment

    def __str__(self):
        return f"City: {self['city']}, Street: {self['street']}, Building: {self['building']}, Apartment: {self['apartment']}"
