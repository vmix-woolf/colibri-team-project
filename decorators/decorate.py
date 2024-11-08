from messages.constants import Constants
from exceptions.exceptions import (
    InvalidNameException,
    EmailNotValidException,
    InvalidDateFormatException,
    InvalidDateValueException,
    PhoneIsAlreadyBelongingException,
    PhoneNumberException, ContactHasBirthdayException, NoSuchContactException, PhoneIsAlreadyBelongToAnotherException, EmailIsAlreadyBelongToAnotherException
)
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except InvalidNameException:
            return Constants.NAME_IS_NOT_VALID.value
        except EmailNotValidException:
            return Constants.EMAIL_IS_NOT_VALID.value
        except InvalidDateFormatException:
            return Constants.INVALID_FORMAT_ERROR.value
        except InvalidDateValueException:
            return Constants.INVALID_DATE_VALUE_ERROR.value
        except PhoneIsAlreadyBelongingException:
            return Constants.PHONE_BELONGS_TO_CONTACT.value
        except PhoneIsAlreadyBelongToAnotherException:
            return Constants.PHONE_BELONG_TO_ANOTHER_CONTACT.value
        except PhoneNumberException:
            return Constants.PRECISE_DIGITS_ERROR.value
        except EmailIsAlreadyBelongToAnotherException:
            return Constants.EMAIL_BELONGS_TO_ANOTHER_CONTACT.value
        except NoSuchContactException:
            return Constants.NO_SUCH_CONTACT.value
        except ContactHasBirthdayException:
            return Constants.CONTACT_HAS_BIRTHDAY.value
        except IndexError as e:
            return str(e)

    return inner