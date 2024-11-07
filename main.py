from handlers.parser import parse_input
from storage.keeper import save_data, load_data
from messages.constants import Constants
from handlers.handler import (
    add_contact, change_contact, show_contacts,
    add_phone, remove_phone, edit_phone,
    add_birthday, change_birthday, birthdays,
    add_address, change_address, remove_address,
    add_email, remove_email, edit_email, show_email
)
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


COMMANDS = [
        "close", "exit", "quit", "hello", "add-contact", "edit-contact", 
        "add-phone", "remove-phone", "edit-phone", "add-birthday", 
        "edit-birthday", "add-address", "edit-address", "remove-address", 
        "birthdays", "add-email", "edit-email", "remove-email", 
        "show-email", "all"
    ]

command_completer = WordCompleter(COMMANDS, ignore_case=True)

def main():
    addressbook = load_data()
    print(Constants.WELCOME_MESSAGE.value)

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
        elif command == "edit-contact":
            print(change_contact(args, addressbook))
        elif command == "remove":
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
        elif command == "all":
            print(show_contacts(addressbook))
        else:
            print(Constants.INVALID_COMMAND_ERROR.value)


if __name__ == "__main__":
    main()