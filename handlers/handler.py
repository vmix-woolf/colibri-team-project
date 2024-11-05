from assistant.addressbook import AddressBook


def show_contacts(addressbook: AddressBook):
    pass

def add_contact(args, addressbook):
    name, phone_number, *_ = args

    if len(args) < 2:
        raise ValueError

def change_contact(addressbook: AddressBook):
    pass

def remove_phone(addressbook: AddressBook):
    pass