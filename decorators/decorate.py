from messages.constants import Constants
from exceptions.exceptions import (
    InvalidNameException,
    EmailNotValidException,
    InvalidDateFormatException,
    InvalidDateValueException, ContactAlreadyExistsException
)
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return Constants.VALUE_ERROR.value
        except InvalidNameException:
            return Constants.NAME_IS_NOT_VALID.value
        except EmailNotValidException:
            return Constants.EMAIL_IS_NOT_VALID.value
        except InvalidDateFormatException:
            return Constants.INVALID_FORMAT_ERROR.value
        except InvalidDateValueException:
            return Constants.INVALID_DATE_VALUE_ERROR.value
        except ContactAlreadyExistsException:
            return Constants.CONTACT_ALREADY_EXISTS.value

    return inner