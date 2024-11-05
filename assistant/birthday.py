import re
import calendar

from assistant.field import Field
from exceptions.exceptions import (
    InvalidDateFormatException,
    InvalidDateValueException
)


class Birthday(Field):

    def __init__(self, value):
        if not self.birthday_format_validation(value):
            raise InvalidDateFormatException

        if not self.birthday_value_validation(value):
            raise InvalidDateValueException

        super().__init__(value)
        self.birthday = value

    @staticmethod
    def birthday_format_validation(birthday):
        return True if bool(re.match(r'\d{1,2}\.\d{1,2}\.\d{4}', birthday)) else False

    @staticmethod
    def birthday_value_validation(birthday):
        day, month, year = birthday.split('.')
        day = int(day)
        month = int(month)
        year = int(year)

        if year < 1 or year > 9999:
            return False

        if month < 1 or month > 12:
            return False

        if day < 1 or day > 31:
            return False

        max_days = calendar.monthrange(year, month)[1]

        if day > max_days:
            return False

        return True