from assistant.name import Name
from assistant.phone import Phone
from decorators.decorate import input_error
from exceptions.exceptions import PhoneNumberException


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = {}
        self.email = None
        self.birthday = None

    @input_error
    def remove_phone(self, phone):
        if not Phone.phone_number_validation(phone):
            raise PhoneNumberException
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                return True
        return False

    @input_error
    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    @input_error
    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    @input_error
    def find_phone(self, phone_number):
        try:
            index = self.phones.index(phone_number)

            return self.phones[index]
        except ValueError:
            return False

    @input_error
    def add_birthday(self, birthday):
        self.birthday = birthday

    @input_error
    def has_birthday(self):
        return True if self.birthday is not None else False

    @input_error
    def edit_birthday(self, new_birthday):
        self.birthday = new_birthday

    def __str__(self):
        basic_message = f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

        if self.email is not None:
            basic_message += f", email: {self.email}"

        if self.birthday is not None:
            basic_message += f", birthday: {self.birthday}"

        if len(self.address) != 0:
            basic_message += f", address: (city: {self.address['city']}; street: {self.address['street']}; house: {self.address['building']}; apartment: {self.address['apartment']})"

        return basic_message