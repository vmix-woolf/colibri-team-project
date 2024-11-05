from assistant.name import Name
from assistant.phone import Phone
from exceptions.exceptions import PhoneNumberException


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = {}
        self.email = None
        self.birthday = None

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        if not Phone.validate(phone):
            raise PhoneNumberException()
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                return True
        return False
    
    def edit_phone(self, old_phone, new_phone):
        if not Phone.validate(new_phone):
            raise PhoneNumberException()        
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                phone_obj.value = new_phone
                return True
        return False
