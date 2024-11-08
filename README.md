# Personal assistant

---

### Description

Здесь будет описание и назначение программы.

### Installing

1. Clone this repository locally
2. Run `python -m pip install -r requirements.txt` for installing dependencies

### Running tests:

1. Run `python -m unittest tests/test_commands.py`

### Command List

`hello` -

#### contacts and phones
`add <contact_name> <phone_number>` - adds **contact name** and their **phone number**

`change <contact_name> <phone_number>` - update **phone number** for the **contact**

`add-phone <contact_name> <phone_number>` - 

`change <contact_name> <old_phone> <new_phone>` -

`remove-phone <contact_name> <phone_number>` - 

`remove <contact_name>` - 

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
`add-note` - first use 'add-note' command, then write title and content of the th note

`search-text <text>` - find note by word in the content

`edit-note <number_key>` - edit note's title and content by it's id

`remove-note <number_key>` - remove note by it's id 

`edit-note title <title>` - 

`remove-note title <title>` - 

#### additionally - tags
`add-tag <title> <#tag>` - add a tag to a note with the given title

`search <#tag>` - search note by tag

`sort <#tag>` - sort notes by the given tag
#### ai
the is will be section on command's prompt


`exit`, `quit`, `close`- exit program and good luck wishes!

