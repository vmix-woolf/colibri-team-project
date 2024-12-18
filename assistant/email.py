import re

from assistant.field import Field
from exceptions.exceptions import (
    EmailNotValidException
)


class Email(Field):

    def __init__(self, value):
        if not self.email_validation(value):
            raise EmailNotValidException
        super().__init__(value)

    @staticmethod
    def email_validation(email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$', email)
    
    def __str__(self):
        return self.value
    