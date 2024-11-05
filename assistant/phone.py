from assistant.field import Field


class Phone(Field):

    def __init__(self, value):
        super().__init__(value)
        self.value = value