from enum import Enum

class Constants(Enum):
    NUMBER_OF_DIGITS_IN_PHONE_NUMBER = 3
    ADDRESS_BOOK_FILE_NAME = "addressbook.pkl"

    WELCOME_MESSAGE = "Welcome to the Personal Assistant bot!"
    INVALID_COMMAND_ERROR = "Invalid command."
    # related to adding process
    CONTACT_ADDED = "Contact is added."
    CONTACT_UPDATED = "Contact is updated."
    CONTACT_DELETED = "Contact is deleted."
    CONTACT_ALREADY_EXISTS = "Contact is already exists."
    PHONE_ADDED = "Phone is added."
    PHONE_UPDATED = "Phone is updated."
    EMAIL_ADDED = "Email is added."
    EMAIL_UPDATED = "Email is updated."
    BIRTHDAY_ADDED = "Birthday is added."
    BIRTHDAY_UPDATED = "Birthday is updated."
    ADDRESS_ADDED = "Address is added."
    NOTE_ADDED = "Note is added."
    # related to errors
    VALUE_ERROR = "Enter the correct argument value."
    # related to contacts
    NAME_IS_NOT_VALID = "Name is not valid."
    NO_CONTACTS = "There are still no contacts."
    NO_SUCH_CONTACT = "No such contact in the address book."
    # related to emails
    EMAIL_IS_NOT_VALID = "Email is not valid."
    # related to the birthday
    INVALID_FORMAT_ERROR = "Invalid date format. Use DD.MM.YYYY"
    INVALID_DATE_VALUE_ERROR = "Invalid date value. Use correct date."