from messages.constants import Constants
from assistant.field import Field


class Phone(Field):

    def __init__(self, value):
        if not self.phone_number_validation(value):
            raise ValueError(Constants.PRECISE_DIGITS_ERROR.value)
        super().__init__(value)

    @staticmethod
    def phone_number_validation(phone_number):
        return isinstance(phone_number, str) and phone_number.isdigit() and len(phone_number) == Constants.NUMBER_OF_DIGITS_IN_PHONE_NUMBER.value

    def __str__(self):
        return self.value