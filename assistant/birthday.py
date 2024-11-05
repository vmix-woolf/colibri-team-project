from assistant.field import Field


class Birthday(Field):

    def __init__(self, value):
        super().__init__(value)
        self.birthday = value