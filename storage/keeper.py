import pickle

from assistant.addressbook import AddressBook
from messages.constants import Constants

def save_data(book, filename=Constants.ADDRESS_BOOK_FILE_NAME.value):
    with open(filename, "wb") as fh:
        # noinspection PyTypeChecker
        pickle.dump(book, fh)


def load_data(filename=Constants.ADDRESS_BOOK_FILE_NAME.value):
    try:
        with open(filename, "rb") as fh:
            return pickle.load(fh)
    except FileNotFoundError:
        return AddressBook()