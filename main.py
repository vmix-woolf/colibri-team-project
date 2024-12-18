from handlers.parser import parse_input
from storage.keeper import save_data, load_data
from messages.constants import Constants
from handlers.handler import (
    add_contact, format_contacts,
    add_phone, remove_phone, edit_phone,
    add_birthday, change_birthday, remove_birthday, birthdays,
    add_address, change_address, remove_address,
    add_email, remove_email, edit_email, show_email, 
    add_note, edit_note, search_note, remove_note,
    show_notes, add_tag, search_tag, sort_by_tag,
    search_by_name, search_by_birthday, search_by_email, remove_contact
)
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from assistant.notebook import Notebook

COMMANDS = [
    "close", "exit", "quit", "hello",
    "add-contact", "edit-contact",
    "add-phone", "edit-phone", "remove-phone",
    "add-birthday", "edit-birthday", "remove-birthday",
    "add-address", "edit-address", "remove-address", "birthdays",
    "add-email", "edit-email", "remove-email", "show-email",
    "search-name", "search-birthday", "search-email",
    "all",
    "add-note", "search-text", "edit-note", "remove-note",
    "add-tag", "search-tag", "sort-tag", "show-notes"
]

command_completer = WordCompleter(COMMANDS, ignore_case=True)

def main():
    addressbook = load_data()
    print(Constants.WELCOME_MESSAGE.value)
    notebook = Notebook()

    while True:
        user_input = prompt("Enter a command: ", completer=command_completer)
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            save_data(addressbook)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add-contact":
            print(add_contact(args, addressbook))
        elif command == "remove-contact":
            print(remove_contact(args, addressbook))
        elif command == "add-phone":
            print(add_phone(args, addressbook))
        elif command == "remove-phone":
            print(remove_phone(args, addressbook))
        elif command == "edit-phone":
            print(edit_phone(args, addressbook))
        elif command == "add-birthday":
            print(add_birthday(args, addressbook))
        elif command == "edit-birthday":
            print(change_birthday(args, addressbook))
        elif command == "remove-birthday":
            print(remove_birthday(args, addressbook))
        elif command == "add-address":
            print(add_address(args, addressbook))
        elif command == "edit-address":
            print(change_address(args, addressbook))
        elif command == "remove-address":
            print(remove_address(args, addressbook))
        elif command == "birthdays":
            print(birthdays(addressbook))
        elif command == "add-email":
            print(add_email(args, addressbook))
        elif command == "edit-email":
            print(edit_email(args, addressbook))
        elif command == "remove-email":
            print(remove_email(args, addressbook))
        elif command == "show-email":
            print(show_email(args, addressbook))
        elif command == "search-name":
            print(format_contacts(search_by_name(args, addressbook), Constants.NO_CONTACTS_WITH_NAME.value))
        elif command == "search-birthday":
            print(format_contacts(search_by_birthday(args, addressbook), Constants.NO_CONTACTS_WITH_BIRTHDAY.value))
        elif command == "search-email":
            print(format_contacts(search_by_email(args, addressbook), Constants.NO_CONTACTS_WITH_EMAIL.value))
        elif command == "all":
            print(format_contacts(addressbook,  Constants.NO_CONTACTS.value))
        elif command == "add-note":
            print(add_note(notebook))
        elif command == "search-text":
            print(search_note(notebook))
        elif command == "edit-note":
            print(edit_note(notebook, args))
        elif command == "remove-note":
            print(remove_note(notebook, args))
        elif command == "add-tag":
            print(add_tag(notebook, args))
        elif command == "search-tag":
            print(search_tag(notebook, args))
        elif command == "sort-tag":
            print(sort_by_tag(notebook, args))
        elif command == "show-notes":
            print(show_notes(notebook))
        else:
            print(Constants.INVALID_COMMAND_ERROR.value)


if __name__ == "__main__":
    main()