from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, contact):
        self.data[contact.name.value] = contact

    def find_record(self, contact_name):
        return self.data.get(contact_name)

    def remove_record(self, contact_name):
        pass