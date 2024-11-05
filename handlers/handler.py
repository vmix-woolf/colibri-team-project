from assistant.addressbook import AddressBook
from assistant.phone import Phone
from assistant.record import Record
from decorators.decorate import input_error
from exceptions.exceptions import PhoneNumberException, ContactAlreadyExistsException, InvalidNameException
from messages.constants import Constants


@input_error
def show_contacts(addressbook: AddressBook):
    if len(addressbook) == 0:
        print(Constants.NO_CONTACTS.value)
    else:
        for _, contact in addressbook.items():
            print(contact)


@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError
    name, phone_number, *_ = args

    record = book.find_record(name)
    if len(name) > 20 or name[0].isdigit():
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
