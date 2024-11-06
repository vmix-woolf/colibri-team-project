import re
from colorama import Fore
from datetime import datetime as dt
from assistant.addressbook import AddressBook
from assistant.birthday import Birthday
from assistant.name import Name
from assistant.phone import Phone
from assistant.record import Record
from decorators.decorate import input_error
from messages.constants import Constants
from exceptions.exceptions import (
    InvalidNameException, PhoneNumberException, PhoneIsAlreadyBelongingException,
    NoSuchContactException, InvalidDateFormatException, InvalidDateValueException, PhoneIsAlreadyBelongToAnotherException
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
    if len(args) < 2:
        raise ValueError
    
    name, phone_number, *_ = args    

    if not Name.name_validation(name):
        raise InvalidNameException

    phone = Phone(phone_number)
    
    record = addressbook.find_record(name)

    if record is None:  # if such name is new
        record = Record(name)
        addressbook.add_record(record)
        record.add_phone(phone)

        return Constants.CONTACT_ADDED.value
    elif record.find_phone(phone_number):  # continue if such name is already kept
        raise PhoneIsAlreadyBelongingException
    else:
        record.add_phone(phone_number)
        return Constants.CONTACT_UPDATED.value

def change_contact(args, addressbook: AddressBook):
    pass

def remove_phone(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Error: You must provide both Name and Phone number.")

    name, phone = args
    record = book.find_record(name)
    if record:
        if record.remove_phone(phone):
            #should be uncomment after save_data will be added
            #save_data(book)
            return f"Phone number {phone} removed from {name}."
        return "Phone number not found."
    return "Contact not found."

@input_error
def add_phone(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Error: You must provide both Name and Phone number.")

    name, phone_number, *_ = args

    if not Name.name_validation(name):
        raise InvalidNameException

    phone = Phone(phone_number)
    record = book.find_record(name)
    if record:
        for _, contact in book.items():
            for existing_phone in contact.phones:
                if existing_phone.value == phone_number and name == contact.name.value:
                    raise  PhoneIsAlreadyBelongingException
                elif existing_phone.value == phone_number:
                    raise PhoneIsAlreadyBelongToAnotherException
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

@input_error
def add_birthday(args, addressbook: AddressBook):
    name, birthday, *_ = args

    if len(args) < 2:
        raise ValueError

    if not Name.name_validation(name):
        raise InvalidNameException

    record = addressbook.find_record(name)

    if record is None:
        raise NoSuchContactException

    if record.has_birthday():
        # raise ContactHasBirthdayException
        return Constants.CONTACT_HAS_BIRTHDAY.value

    if not Birthday.birthday_format_validation(birthday):
        raise InvalidDateFormatException

    if not Birthday.birthday_value_validation(birthday):
        raise InvalidDateValueException
    else:
        record.add_birthday(birthday)

        return Constants.BIRTHDAY_ADDED.value

@input_error
def change_birthday(args, addressbook: AddressBook):
    name, new_birthday, *_ = args

    if len(args) < 2:
        raise ValueError

    if not Name.name_validation(name):
        raise InvalidNameException

    record = addressbook.find_record(name)

    if record is None:
        return Constants.NO_SUCH_CONTACT.value

    if not record.has_birthday():
        return Constants.CONTACT_HAS_NOT_BIRTHDAY.value

    if not Birthday.birthday_format_validation(new_birthday):
        raise InvalidDateFormatException

    if not Birthday.birthday_value_validation(new_birthday):
        raise InvalidDateValueException
    else:
        record.edit_birthday(new_birthday)

        return Constants.BIRTHDAY_UPDATED.value

@input_error
def birthdays(addressbook):
    days_qty = input(Fore.LIGHTGREEN_EX + "Enter the number of days in which the birthday is to occur: " + Fore.YELLOW)
    if not (re.match(r'\d+', days_qty) and days_qty != 0):
        return Constants.NATURAL_NUMBER_ERROR.value

    if len(addressbook) == 0:
        print(Constants.CONTACT_LIST_EMPTY.value)
    else:
        today = dt.today().date()

        for record in addressbook.values():
            if record.birthday is None:
                continue

            birthday_date = dt.strptime(record.birthday, "%d.%m.%Y")
            birthday_this_year = birthday_date.date().replace(year=today.year)

            if birthday_this_year < today:
                next_birthday = birthday_this_year.replace(year=today.year + 1)
            else:
                next_birthday = birthday_this_year

            if (next_birthday - today).days <= int(days_qty):
                print(Fore.RESET, record)
            else:
                continue
        else:
            return Constants.NO_NECESSARY_TO_CONGRATULATE.value

@input_error
def add_address(args, addressbook: AddressBook):
    name, *_ = args

    if len(args) < 1:
        raise ValueError

    record = addressbook.find_record(name)

    if record is None:
        raise NoSuchContactException

    if record.has_address():
        return Constants.ADDRESS_IS_ALREADY_PRESENT.value
    else:
        city = input('Type the name of the city: ')
        street = input('Type the name of the street: ')
        building = input('Type a number of the building: ')
        apartment = int(input('Type a number of the apartment: '))
        address = {
            'city': city if city else 'N/A',
            'street': street if street else 'N/A',
            'building': building if building else 'N/A',
            'apartment': apartment if apartment else 'N/A',
        }

        record.add_address(address)

        return Constants.ADDRESS_ADDED.value

@input_error
def change_address(args, addressbook: AddressBook):
    name, *_ = args

    if len(args) < 1:
        raise ValueError

    record = addressbook.find_record(name)

    if record is None:
        return Constants.NO_SUCH_CONTACT.value

    city = input('Type the name of the city: ')
    street = input('Type the name of the street: ')
    building = input('Type a number of the building: ')
    apartment = input('Type a number of the apartment: ')
    address = {
        'city': city if city else 'N/A',
        'street': street if street else 'N/A',
        'building': building if building else 'N/A',
        'apartment': apartment if apartment else 'N/A',
    }

    record.edit_address(address)

    return Constants.ADDRESS_UPDATED.value

@input_error
def remove_address(args, addressbook: AddressBook):
    name, *_ = args

    if len(args) < 1:
        raise ValueError

    record = addressbook.find_record(name)

    if record is None:
        return Constants.NO_SUCH_CONTACT.value

    if not record.has_address():
        return Constants.CONTACT_HAS_NO_ADDRESS.value
    else:
        record.remove_address()

        return Constants.ADDRESS_DELETED.value
