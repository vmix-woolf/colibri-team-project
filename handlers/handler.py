import re
from colorama import Fore
from datetime import datetime as dt
from assistant.addressbook import AddressBook
from assistant.birthday import Birthday
from assistant.address import Address
from assistant.name import Name
from assistant.phone import Phone
from assistant.email import Email
from assistant.record import Record
from decorators.decorate import input_error
from messages.constants import Constants
from exceptions.exceptions import (
    InvalidNameException, PhoneNumberException, PhoneIsAlreadyBelongingException,
    NoSuchContactException, InvalidDateFormatException, InvalidDateValueException,
    PhoneIsAlreadyBelongToAnotherException, EmailIsAlreadyBelongToAnotherException, EmailNotValidException
)
from helpers import format_table

@input_error
def format_contacts(contacts, error_message):
    if contacts is None:
        return error_message
    if isinstance(contacts, str):
        return contacts
    if isinstance(contacts, Record):
        records_list = [contacts]
    else:
        records_list = list(contacts)
    if len(records_list) == 0:
        return error_message
    else:
        fields = ["Name", "Phones", "Address", "Email", "Birthday"]
        return format_table(fields, records_list)

@input_error
def add_contact(args, addressbook):
    if len(args) < 2:
        raise ValueError("Error: You must provide both Name and Phone number.")
    
    name, phone_number, *_ = args    

    if not Name.name_validation(name):
        raise InvalidNameException

    phone = Phone(phone_number)
    record = addressbook.find_record(name)

    if record:
        if record.find_phone(phone):
            raise PhoneIsAlreadyBelongingException
        else: 
            record.add_phone(phone)
            return Constants.CONTACT_UPDATED.value
    else:
        if addressbook.find_by_phone(phone):
            raise PhoneIsAlreadyBelongToAnotherException
        else:
            record = Record(name)
            addressbook.add_record(record)
            record.add_phone(phone)
            return Constants.CONTACT_ADDED.value

def remove_contact(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("You must provide Name")

    name, *_ = args

    record = book.find_record(name)
    if record:
        book.remove_record(name)

        return Constants.CONTACT_DELETED.value

    return Constants.NO_SUCH_CONTACT.value

def change_contact(args, addressbook: AddressBook):
    pass

@input_error
def remove_phone(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Error: You must provide both Name and Phone number.")

    name, phone_number, *_ = args 
    if not Phone.phone_number_validation(phone_number):
        raise PhoneNumberException
    
    record = book.find_record(name)
    phone = Phone(phone_number)
    if record:
        if record.remove_phone(phone):
            return f"Phone number {phone_number} removed from {name}."
        return "Phone number not found."
    return "Contact not found."

@input_error
def add_phone(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Error: You must provide both Name and Phone number.")

    name, phone_number, *_ = args

    phone = Phone(phone_number)
    record = book.find_record(name)

    if not record:
        return Constants.NO_SUCH_CONTACT.value
    
    existing_record = book.find_by_phone(phone)

    if existing_record:
        if existing_record.name.value == name:
            raise PhoneIsAlreadyBelongingException
        else:
            raise PhoneIsAlreadyBelongToAnotherException

    record.add_phone(phone)
    return Constants.PHONE_ADDED.value

@input_error
def edit_phone(args, addressbook: AddressBook):
    if len(args) < 3:
        raise ValueError("Error: You must provide Name, Old number and New one.")

    name, old_phone_number, new_phone_number, *_ = args

    if not Phone.phone_number_validation(old_phone_number):
        raise PhoneNumberException

    old_phone = Phone(old_phone_number)
    new_validated_phone = Phone(new_phone_number)
    record = addressbook.find_record(name)

    if not record:
        return Constants.NO_SUCH_CONTACT.value
    else:
        if not record.find_phone(old_phone):
            return Constants.PHONE_NO_BELONGS_TO_THIS_CONTACT.value
        else:
            record.edit_phone(old_phone, new_validated_phone)
            return Constants.PHONE_UPDATED.value    

@input_error
def add_birthday(args, addressbook: AddressBook):
    if len(args) < 2:
        raise ValueError("Error: You must provide both Name and Birthday.")
    
    name, birthday, *_ = args

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
       return Constants.CONTACT_LIST_EMPTY.value
    else:
        today = dt.today().date()
        result = []
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
                result.append(record)
            else:
                continue
        if not result:
            return Constants.NO_NECESSARY_TO_CONGRATULATE.value
        
    fields = ["Name", "Phones", "Address", "Email", "Birthday"]
    return format_table(fields, result)

@input_error
def add_address(args, addressbook: AddressBook):
    if len(args) < 1:
        raise ValueError("Error: You must provide Name")
    
    name, *_ = args   

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

        address_obj = Address(address['city'], address['street'], address['building'], address['apartment'])
        print(address_obj)

        record.add_address(address_obj)

        return Constants.ADDRESS_ADDED.value

@input_error
def change_address(args, addressbook: AddressBook):
    if len(args) < 1:
        raise ValueError("Error: You must provide Name")

    name, *_ = args

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
    if len(args) < 1:
        raise ValueError("Error: You must provide Name")

    name, *_ = args

    record = addressbook.find_record(name)

    if record is None:
        return Constants.NO_SUCH_CONTACT.value

    if not record.has_address():
        return Constants.CONTACT_HAS_NO_ADDRESS.value
    else:
        record.remove_address()

        return Constants.ADDRESS_DELETED.value

@input_error
def add_email(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Error: You must provide both Name and Email number.")

    name, email, *_ = args
    email_obj = Email(email)
    record = book.find_record(name)
    if not record:
        return Constants.NO_SUCH_CONTACT.value
    
    if record.email:
        raise ValueError("The contact already has an email. You can edit it or remove.")
    
    for _, contact in book.items():
        if contact.email and contact.email.value == email:
            raise EmailIsAlreadyBelongToAnotherException("This email is already assigned to another contact.")
        
    record.add_email(email_obj)
    return Constants.EMAIL_ADDED.value

@input_error
def remove_email(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("Error: You must provide Name")
    
    name, *_ = args
    record = book.find_record(name)

    if not record:
        return Constants.NO_SUCH_CONTACT.value
    
    if record.email.value:
        removed_email = record.remove_email()
        return f"{removed_email} {Constants.EMAIL_REMOVED.value}"
    else:
        raise ValueError("This contact doesn't have such email")

@input_error
def edit_email(args, book: AddressBook):
    if len(args) < 3:
        raise ValueError("Error: You must provide Name, Old email and New one.")
    
    name, old_email, new_email, *_ = args
    record = book.find_record(name)

    if not record:
        return Constants.NO_SUCH_CONTACT.value
    
    if not Email.email_validation(old_email):
        raise PhoneNumberException
    
    email_obj_new = Email(new_email)

    if not record.email:
        raise ValueError("This contact doesn't have an email. Please add one first.")

    if record.email.value != old_email:
        raise ValueError("The provided old email does not match the current email of this contact.")

    for _, contact in book.items():
        if contact.email and contact.email.value == new_email:
            raise EmailIsAlreadyBelongToAnotherException("This new email is already assigned to another contact.")

    record.edit_email(record.email, email_obj_new)
    return Constants.EMAIL_UPDATED.value

@input_error
def show_email(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("Error: You must provide Name")
    
    name, *_ = args
    record = book.find_record(name)
    
    if not record:
        return Constants.NO_SUCH_CONTACT.value
    
    if not record.email:
        raise ValueError("This contact doesn't have an email. Please add one first.")
    
    return record.show_email()

@input_error
def search_by_name(args, addressbook: AddressBook):
    if len(args) < 1:
        raise ValueError("You must provide Name")

    name, *_ = args

    return addressbook.find_record(name)

@input_error
def search_by_birthday(args, addressbook: AddressBook):
    if len(args) < 1:
        raise ValueError("You must provide Birthday")

    birthday, *_ = args

    if not Birthday.birthday_format_validation(birthday):
        raise InvalidDateFormatException

    if not Birthday.birthday_value_validation(birthday):
        raise InvalidDateValueException

    return addressbook.find_by_birthday(birthday)

@input_error
def search_by_email(args, addressbook: AddressBook):
    if len(args) < 1:
        raise ValueError("You must provide Email")

    email, *_ = args

    if not Email.email_validation(email):
        raise EmailNotValidException

    return addressbook.find_by_email(email)