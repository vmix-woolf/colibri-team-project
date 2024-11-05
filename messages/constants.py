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
    EMAIL_ADDED = "Email is added."
    EMAIL_UPDATED = "Email is updated."
    BIRTHDAY_ADDED = "Birthday is added."
    BIRTHDAY_UPDATED = "Birthday is updated."
    ADDRESS_ADDED = "Address is added."
    NOTE_ADDED = "Note is added."