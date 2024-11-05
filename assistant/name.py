from field import Field

class Name(Field):

    def __init__(self, value):
        super().__init__(value)
        self.value = value