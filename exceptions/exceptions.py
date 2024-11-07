class InvalidNameException(Exception):
    pass

class EmailNotValidException(Exception):
    pass

class InvalidDateFormatException(Exception):
    pass

class InvalidDateValueException(Exception):
    pass

class PhoneNumberException(Exception):
    pass

class PhoneIsAlreadyBelongingException(Exception):
    pass

class PhoneIsAlreadyBelongToAnotherException(Exception):
    pass

class NoSuchContactException(Exception):
    pass

class ContactHasBirthdayException(Exception):
    pass
