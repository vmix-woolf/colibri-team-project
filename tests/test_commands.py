import unittest
from handlers.handler import add_contact
from assistant.addressbook import AddressBook
from assistant.record import Record
from exceptions.exceptions import InvalidNameException, PhoneIsAlreadyBelongingException, PhoneIsAlreadyBelongToAnotherException
from messages.constants import Constants

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.addressbook = AddressBook()

    def test_add_contact_success(self):
        args = ["John", "333"]
        result = add_contact(args, self.addressbook)
        self.assertEqual(result, Constants.CONTACT_ADDED.value)

        contact = self.addressbook.find_record("John")
        self.assertIsNotNone(contact)
        self.assertEqual(contact.name.value, "John")
        self.assertEqual(contact.phones[0].value, "333")

    def test_add_duplicated_contact(self):
        args1 = ["John", "333"]
        add_contact(args1, self.addressbook)
        args2 = ["John", "333"]
        result = add_contact(args2, self.addressbook)

        self.assertEqual(result, Constants.PHONE_BELONGS_TO_CONTACT.value)

    def test_add_contact_with_existing_phone_in_another_contact(self):
        args1 = ["John", "333"]
        add_contact(args1, self.addressbook)
        args2 = ["Jane", "333"]
        result = add_contact(args2, self.addressbook)

        self.assertEqual(result, Constants.PHONE_BELONG_TO_ANOTHER_CONTACT.value)
        
    def test_add_invalid_name(self):
        args = ["", "333"]
        result = add_contact(args, self.addressbook)

        self.assertEqual(result, Constants.NAME_IS_NOT_VALID.value)

    def test_add_invalid_phone(self):
        args = ["John", "invalid_phone"]        
        result = add_contact(args, self.addressbook)

        self.assertEqual(result, "Phone number must be exactly 10 digits.")

    def test_add_one_parameter(self):
        args = ["John"]
        result = add_contact(args, self.addressbook)
        self.assertEqual(result, 'Error: You must provide both Name and Phone number.')

    def test_add_unique_phone_to_same_name(self):
        args1 = ["John", "333"]
        add_contact(args1, self.addressbook)
        args2 = ["John", "334"]
        result = add_contact(args2, self.addressbook)
        self.assertEqual(result, Constants.CONTACT_UPDATED.value)
