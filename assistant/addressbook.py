from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, contact):
        record_indices = self.data.keys()
        if len(record_indices) == 0:
            self.data[0] = contact
        else:
            self.data[max(record_indices) + 1] = contact

    def find_record(self, contact_name):
        for _, record in self.data.items():
            if record.name.value == contact_name:
                return record

    def remove_record(self, contact_name):
        record_key = 0
        for key, record in self.data.items():
            if record.name.value == contact_name:
                record_key = key
        del self.data[record_key]

    # def find_by_phone(self, phone):
    #     for record in self.data.values():
    #         if record.find_phone(phone) is not None:
    #             return record
    #     return False

    def find_by_birthday(self, birthday):
        contacts = []
        for _, record in self.data.items():
            if record.birthday == birthday:
                contacts.append(record)
        return contacts

    def find_by_email(self, email):
        for _, record in self.data.items():
            if record.email is not None and record.email.value == email:
                return record
        return None