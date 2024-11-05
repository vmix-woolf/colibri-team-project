from assistant.addressbook import AddressBook
from decorators.decorate import input_error
from messages.constants import Constants


@input_error
def show_contacts(addressbook: AddressBook):
    if len(addressbook) == 0:
        print(Constants.NO_CONTACTS.value)
    else:
        for _, contact in addressbook.items():
            print(contact)

def add_contact(args, addressbook):
    name, phone_number, *_ = args

    if len(args) < 2:
        raise ValueError

def change_contact(args, addressbook: AddressBook):
    pass

def remove_phone(args, addressbook: AddressBook):
    pass