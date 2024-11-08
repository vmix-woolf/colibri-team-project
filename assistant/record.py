from assistant.name import Name
from decorators.decorate import input_error


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = {}
        self.email = None
        self.birthday = None

    def remove_phone(self, phone):
        for phone_item in self.phones:
            if phone_item.value == phone.value:
                self.phones.remove(phone_item)
                return True
        return False

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def edit_phone(self, old_phone, new_phone):

        for phone_item in self.phones:
            if phone_item.value == old_phone.value:
                self.remove_phone(old_phone)
                self.add_phone(new_phone)

    def find_phone(self, phone):
        for phone_item in self.phones:
            if phone.value == phone_item.value:
                return phone
        return None

    def add_email(self, email):
        if not self.email:
            self.email = email
            return True
        return False
    
    def show_email(self):
        return self.email.value

    def remove_email(self):
        removed_value = self.email.value
        if self.email.value:
            self.email = None
            return removed_value
        return False

    def edit_email(self, old_email, new_email):
        if self.email.value == old_email.value:
            if self.remove_email():
                self.add_email(new_email)
                return True        
        return False

    @input_error
    def add_birthday(self, birthday):
        self.birthday = birthday

    @input_error
    def has_birthday(self):
        return True if self.birthday is not None else False

    @input_error
    def remove_birthday(self):
        self.birthday = None

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
            basic_message += f", address: {str(self.address)}"

        return basic_message