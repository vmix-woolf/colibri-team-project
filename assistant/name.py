import re

from assistant.field import Field

class Name(Field):

    def __init__(self, value):
        if not self.name_validation(value):
            raise ValueError('Name cannot be empty')
        super().__init__(value)

    @staticmethod
    def name_validation(name):
        return True if bool(re.match(r'^[A-Za-z]{2,20}$', name)) else False