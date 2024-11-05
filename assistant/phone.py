from assistant.field import Field
from exceptions.exceptions import PhoneNumberException


class Phone(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise PhoneNumberException()
        super().__init__(value)

    @staticmethod
    def validate(phone):
        return phone.isdigit() and len(phone) == 10
    
    @staticmethod
    def format_phone(phone):
        return f"+38 ({phone[:3]}) {phone[3:6]} {phone[6:8]} {phone[8:]}"