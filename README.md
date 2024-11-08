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

`change <contact_name> <phone_number>` - update **phone number** for the **contact**

`remove <contact_name>` - 

`add-phone <contact_name> <phone_number>` - 

`change <contact_name> <old_phone> <new_phone>` -

`remove-phone <contact_name> <phone_number>` - 



`all` - 
#### emails
`add-email <contact_name> <email>` - 

`change-email <contact_name> <email>` -
#### address
`add-address <contact_name>` -

`change-address <contact_name>` - 

`remove-address <contact_name>` -
#### birthdays
`add-birthday <contact_name> <bd_date>` - 

`change-birthday <contact_name> <refined_bd>` - 

`remove-birthday <contact-name>` - 

`birthdays` -
#### search
`search <contact_name>` - 

`search-email <email>` -

`search-birthday <db_date>` -
#### notes
`add-note` - 

`search-text <text>` -

`edit-note <number_key>` -

`remove-note <number_key>` -

`edit-note title <title>` -

`remove-note title <title>` -

#### additionally - tags
`add-tag <title> <#tag>` -

`search <#tag>` -

`sort <#tag>`
#### ai
the is will be section on command's prompt


`exit`, `quit`, `close`- exit program and good luck wishes!

