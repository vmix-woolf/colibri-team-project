from messages.constants import Constants
from assistant.field import Field


class Phone(Field):

    def __init__(self, value):
        if not self.phone_number_validation(value):
            raise ValueError()
        super().__init__(value)

    @staticmethod
    def phone_number_validation(phone_number):
        return True if phone_number.isdigit() and len(phone_number) == Constants.NUMBER_OF_DIGITS_IN_PHONE_NUMBER.value else False
