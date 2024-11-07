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

    def remove_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                return True
        return False

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.remove_phone(old_phone)
                self.add_phone(new_phone)
                return True
        return False

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number.value:
                return phone
        return False

    def add_email(self, email):
        if not self.email:
            self.email = email
            return True
        return False

    def remove_email(self, email):
        if self.email.value == email.value:
            self.email = None
            return True
        return False

    def edit_email(self, old_email, new_email):
        if self.remove_email(old_email):
            self.add_email(new_email)


    @input_error
    def add_birthday(self, birthday):
        self.birthday = birthday

    @input_error
    def has_birthday(self):
        return True if self.birthday is not None else False

    @input_error
    def edit_birthday(self, new_birthday):
        self.birthday = new_birthday

    @input_error
    def add_address(self, address):
        self.address = address

    @input_error
    def edit_address(self, new_address):
        self.address = new_address

    @input_error
    def has_address(self):
        return False if len(self.address) == 0 else True

    @input_error
    def remove_address(self):
        self.address = {}
    def __str__(self):
        basic_message = f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

        if self.email is not None:
            basic_message += f", email: {self.email}"

        if self.birthday is not None:
            basic_message += f", birthday: {self.birthday}"

        if len(self.address) != 0:
            basic_message += f", address: (city: {self.address['city']}; street: {self.address['street']}; house: {self.address['building']}; apartment: {self.address['apartment']})"

        return basic_message