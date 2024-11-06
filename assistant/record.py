from assistant.name import Name
from assistant.phone import Phone
from decorators.decorate import input_error
from exceptions.exceptions import PhoneNumberException


@input_error
class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = {}
        self.email = None
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def remove_phone(self, phone):
        # TODO: нужно разобраться с валидацией такого метода у нас нет
        if not Phone.validate(phone):
            raise PhoneNumberException
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                return True
        return False
    
    def edit_phone(self, old_phone, new_phone):
        # TODO: нужно разобраться с валидацией такого метода у нас нет
        if not Phone.validate(new_phone):
            raise PhoneNumberException
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                phone_obj.value = new_phone
                return True
        return False

    def __str__(self):
        basic_message = f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

        if self.email is not None:
            basic_message += f", email: {self.email}"

        if self.birthday is not None:
            basic_message += f", birthday: {self.birthday}"

        if len(self.address) != 0:
            basic_message += f", address: (city: {self.address['city']}; street: {self.address['street']}; house: {self.address['building']}; apartment: {self.address['apartment']})"

        return basic_message