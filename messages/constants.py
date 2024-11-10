from enum import Enum

class Constants(Enum):
    NUMBER_OF_DIGITS_IN_PHONE_NUMBER = 10
    NUMBER_OF_DAYS_IN_THE_YEAR = 366
    ADDRESS_BOOK_FILE_PKL = "addressbook.pkl"
    NOTEBOOK_FILE_PKL = "notebook.pkl"

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
    EMAIL_REMOVED = "Email removed."
    EMAIL_UPDATED = "Email is updated."
    BIRTHDAY_ADDED = "Birthday is added."
    BIRTHDAY_UPDATED = "Birthday is updated."
    BIRTHDAY_DELETED = "Birthday is deleted."
    ADDRESS_ADDED = "Address is added."
    ADDRESS_UPDATED = "Address is updated."
    ADDRESS_DELETED = "Address is deleted."
    NOTE_ADDED = "Note is added."
    # related to errors
    VALUE_ERROR = "Enter the correct argument value."
    # related to contacts
    NAME_IS_NOT_VALID = "Name is not valid."
    NO_CONTACTS = "There are still no contacts."
    NO_SUCH_CONTACT = "No such contact in the address book."
    NO_CONTACTS_WITH_BIRTHDAY = "There are no contacts with current birthday."
    NO_CONTACTS_WITH_EMAIL = "There are no contacts with current email."
    NO_CONTACTS_WITH_NAME = "There are no contacts with current name."
    CONTACT_LIST_EMPTY = "Contact list is empty."
    CONTACT_HAS_NO_ADDRESS = "This contact has no address."
    # related to emails
    EMAIL_IS_NOT_VALID = "Email is not valid."
    EMAIL_BELONGS_TO_ANOTHER_CONTACT = "This email already belongs to another contact."
    EMAIL_BELONGS_TO_CONTACT = "This email already belongs to this contact."
    # related to phone
    PHONE_BELONGS_TO_CONTACT = "This phone number already belongs to this contact."
    PHONE_NO_BELONGS_TO_THIS_CONTACT = "The phone doesn't belong to this contact"
    PHONE_BELONG_TO_ANOTHER_CONTACT = "This phone number already belongs to another contact."
    PRECISE_DIGITS_ERROR = f"Phone number must be exactly {NUMBER_OF_DIGITS_IN_PHONE_NUMBER} digits!"
    # related to the birthday
    INVALID_FORMAT_ERROR = "Invalid date format. Use DD.MM.YYYY"
    INVALID_DATE_VALUE_ERROR = "Invalid date value. Use correct date."
    CONTACT_HAS_BIRTHDAY = "This contact has already their birthday."
    CONTACT_HAS_NOT_BIRTHDAY = "This contact has not their birthday yet. Use the command 'add-birthday' to add a birthday.'"
    NATURAL_NUMBER_ERROR = f"The number of days must be a natural number within {NUMBER_OF_DAYS_IN_THE_YEAR} days."
    TITLE_TO_CONGRATULATE = "It's necessary to congratulate the following contacts:"
    NO_NECESSARY_TO_CONGRATULATE = "There are no contacts to be mailed in the coming days."
    # related to address
    ADDRESS_IS_ALREADY_PRESENT = "This contact has an address already. To change it please use 'edit-address' command."
    # related to notes
    NO_NOTES_AVAILABLE = "No notes available!"
    NO_NOTES_FOUND = "No notes found with the given text."
    NOTE_NUM_EDITED = "Note number has been edited."
    NOTE_REMOVED = "Note has been removed."
    NOTE_NOT_FOUND = "Note not found."
    NO_NOTES_START_FRESH = "No existing notes found, starting fresh."
    NOTES_SAVED = "Notes saved."
    INVALID_NOTE_KEY = "Please provide a valid note key."
    TAG_ADDED_TO_NOTE = "Tag has been added."
    SEARCH_RESULTS = "Search results"
    NO_TITLE_AND_TAG = "Please provide title and tag."
    TAG_ALREADY_EXISTS = "Tag has already been added to the note."
    TAG_DOES_NOT_EXIST = "Such tag does not exist."
    TOO_MANY_RESULTS = "Too many results."
    NO_TAG_GIVEN = "Please, provide a tag to look for!"
    NO_KEY_GIVEN = "You need to provide key for the note you want to remove!"