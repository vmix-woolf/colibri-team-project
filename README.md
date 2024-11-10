# Personal assistant
---

### Description

Personal Assistant , implemented as commands in the command line interface, is used to store information about contacts. Unique names, phone numbers, emails, birthdays, addresses are stored. It is also possible to store free-form notes in the form of tact records. 

### Installing

1. Clone this repository locally
2. Run `python -m pip install -r requirements.txt` for installing dependencies

### Running tests:

1. Run `python -m unittest tests/test_commands.py`

### Command List

`hello` - welcome message

#### contacts and phones
`add <contact_name> <phone_number>` - adds **contact name** and their **phone number**

`remove <contact_name>` - remove **contact** by name

`add-phone <contact_name> <phone_number>` - add **phone** to contact

`edit-phone <contact_name> <old_phone_number> <new_phone_number>` - update **phone number** for the **contact**

`remove-phone <contact_name> <phone_number>` - remove **phone** for contact

`all` - show all contacts with names, phones, addresses, emails, birthdays
#### emails
`add-email <contact_name> <email>` - add **email** to contact

`change-email <contact_name> <email>` - replace **email** for contact

`show-email <contact_name>` - display **email** for contact
#### address
`add-address <contact_name>` - add **address** for contact

`edit-address <contact_name>` - edit **address** for contact

`remove-address <contact_name>` - remove **address** for contact
#### birthdays
`add-birthday <contact_name> <bd_date>` - add **birthday** for contact

`edit-birthday <contact_name> <refined_bd>` - update **birthday** for contact 

`remove-birthday <contact-name>` - remove **birthday** for contact

`birthdays` -
#### search
`search-name <contact_name>` - search **contact** by their name

`search-email <email>` - search **contact** by their email

`search-birthday <db_date>` - search **contact** by their birthday
#### notes
`add-note` - add-note, provide title and content of the note

`search-text <text>` - search **note** by text

`edit-note <number_key>` - edit note's title and content by its id

`remove-note <number_key>` - remove note by its id 

`show-notes` - show all notes

#### additionally - tags
`add-tag <title> <#tag>` - add a tag to a **note** with the given title

`search <#tag>` - search **note** by tag

`sort <#tag>` - sort notes by the given tag
#### ai
there is such functionality that tells which commands the scheduler user can enter

---
`exit`, `quit`, `close`- exit program and good luck wishes!

