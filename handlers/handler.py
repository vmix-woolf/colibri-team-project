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

#Функціх для роботи із нотатками
def add_note(manager):
    # Додавання нотатки
    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")
    manager.add_note(title, content)

def search_note(manager):
    # Пошук нотатки за текстом
    text = input("Enter text to search for: ")
    manager.search_text(text)

def edit_note(manager, args):
    # Редагування нотатки за ключем
    try:
        key = args[0]
        title = input("Enter new title (leave empty to keep current): ")
        content = input("Enter new content (leave empty to keep current): ")
        manager.edit_note(int(key), title or None, content or None)
    except IndexError:
        print("Please provide a valid note key.")

def remove_note(manager, args):
    # Видалення нотатки за ключем
    try:
        key = int(args[0])
        manager.remove_note(key)
    except IndexError:
        print("Please provide a valid note key.")

def add_tag(manager, args):
        # Додавання тегу до нотатки
    if len(args) == 2:
        title = args[0]
        tag = args[1]
        manager.add_tag_to_note(title, tag)
    else:
        print("Please provide title and tag.")

def search_tag(manager, args):
    # Пошук нотаток за тегом
    tag = args[0]
    manager.search_by_tag(tag)

def sort_by_tag(manager, args):
    # Сортування нотаток за тегом
    try:
        tag = args[0]
        manager.sort_by_tag(tag)
    except IndexError as e:
        print(e) 

def show_notes(manager):
    manager.show_all_notes()