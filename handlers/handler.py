from assistant.addressbook import AddressBook
from assistant.record import Record

def show_contacts(addressbook: AddressBook):
    pass

def add_contact(args, addressbook):
    name, phone_number, *_ = args

    if len(args) < 2:
        raise ValueError

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
    name, phone = args
    record = book.find_record(name)
    if record:
        try:
            record.add_phone(phone)
            # should be uncomment after save_data will be added
            # save_data(book)
            return f"Phone number {phone} added to {name}."
        except ValueError as e:
            return str(e)
    return "Contact not found."

def edit_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find_record(name)
    if record and record.edit_phone(old_phone, new_phone):
        # should be uncomment after save_data will be added
        #save_data(book)
        return "Phone number updated."
    return "Contact not found or old phone number does not match."
