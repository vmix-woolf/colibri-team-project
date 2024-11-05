from handlers.parser import parse_input
from storage.keeper import save_data, load_data
from messages.constants import Constants
from handlers.handler import (
    add_contact,
    change_contact,
    remove_phone,
    show_contacts,
    edit_phone,
    add_phone
)

def main():
    book = load_data()
    print(Constants.WELCOME_MESSAGE.value)

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            save_data(book)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "add-phone":
            print(add_phone(args, book))
        elif command == "remove-phone":
            print(remove_phone(args, book))
        elif command == "edit-phone":
            print(edit_phone(args, book))
        elif command == "all":
            show_contacts(book)
        else:
            print(Constants.INVALID_COMMAND_ERROR.value)


if __name__ == "__main__":
    main()