from assistant.name import Name


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = {}
        self.email = None
        self.birthday = None