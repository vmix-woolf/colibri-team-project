from handlers.parser import parse_input
from storage.keeper import save_data, load_data
from messages.constants import Constants
from handlers.handler import (
    add_contact,
    change_contact,
    remove_phone,
    show_contacts,
    edit_phone,
    add_phone,
    add_note,
    search_note,
    edit_note,
    remove_note,
    add_tag,
    search_tag,
    sort_by_tag,
    show_notes
)
from assistant.notemanager import NoteManager

def main():
    book = load_data()
    print(Constants.WELCOME_MESSAGE.value)
    manager = NoteManager()

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
        #Команди для роботи з нотатками
        elif command == "add-note":
            add_note(manager)

        elif command == "search-text":
            search_note(manager)

        elif command == "edit-note":
            edit_note(manager, args)

        elif command == "remove-note":
            remove_note(manager, args)

        elif command == "add-tag":
            add_tag(manager, args)

        elif command == "search":
            search_tag(manager, args)

        elif command == "sort":
            sort_by_tag(manager, args)

        elif command == "show-notes":
            show_notes(manager)

        else:
            print(Constants.INVALID_COMMAND_ERROR.value)


if __name__ == "__main__":
    main()