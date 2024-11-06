from assistant.addressbook import AddressBook
from assistant.name import Name
from assistant.phone import Phone
from assistant.record import Record
from decorators.decorate import input_error
from exceptions.exceptions import PhoneNumberException, ContactAlreadyExistsException, InvalidNameException
from messages.constants import Constants
from exceptions.exceptions import (
    InvalidNameException,
    PhoneNumberException,
    PhoneIsAlreadyBelongingException
)


@input_error
def show_contacts(addressbook: AddressBook):
    if len(addressbook) == 0:
        print(Constants.NO_CONTACTS.value)
    else:
        for _, contact in addressbook.items():
            print(contact)

@input_error
def add_contact(args, addressbook):
    name, phone_number, *_ = args


@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError
    name, phone_number, *_ = args

    if Name.name_validation(name):
        record = book.find_record(name)
    else:
        raise InvalidNameException()

    if record is None:
        if Phone.phone_number_validation(phone_number):
            record = Record(name)
            record.add_phone(phone_number)
            book.add_record(record)

            return Constants.CONTACT_ADDED.value
        else:
            raise PhoneNumberException()
    else:
        raise ContactAlreadyExistsException()

    if not Name.name_validation(name):
        raise InvalidNameException

    if not Phone.phone_number_validation(phone_number):
        raise PhoneNumberException

    record = addressbook.find_record(name)

    if record is None:  # if such name is new
        record = Record(name)
        addressbook.add_record(record)
        record.add_phone(phone_number)

        return Constants.CONTACT_ADDED.value
    elif record.find_phone(phone_number):  # continue if such name is already kept
        raise PhoneIsAlreadyBelongingException
    else:
        record.add_phone(phone_number)
        return Constants.CONTACT_UPDATED.value

def change_contact(args, addressbook: AddressBook):
    pass

def remove_phone(args, book: AddressBook):
    name, phone = args
    record = book.find_record(name)
    if record:
        if record.remove_phone(phone):
            #should be uncomment after save_data will be added
            #save_data(book)
            return f"Phone number {phone} removed from {name}."
        return "Phone number not found."
    return "Contact not found."

def add_phone(args, book: AddressBook):
    name, phone, *_ = args

    if len(args) < 2:
        raise ValueError

    record = book.find_record(name)
    if record:
        record.add_phone(phone)
        # should be uncomment after save_data will be added
        # save_data(book)
        return Constants.PHONE_ADDED.value

    return Constants.NO_SUCH_CONTACT.value

def edit_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find_record(name)
    if record and record.edit_phone(old_phone, new_phone):
        # should be uncomment after save_data will be added
        #save_data(book)
        return Constants.PHONE_UPDATED.value
    # TODO: разделить нужно эти две причины либо контакт не найден, либо номер не соответствует
    return "Contact not found or old phone number does not match."
