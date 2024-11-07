from prettytable import PrettyTable
from assistant.record import Record

def format_table(fields: list, results: list):
    table = PrettyTable()
    table.field_names = fields
    for record in results:
        if not isinstance(record, Record):
            raise ValueError('It is not the object of Record')
        row = []

        for field in fields:
            if field == "Name":
                row.append(record.name.value)
            elif field == "Phones":
                phones = ', '.join(str(phone) for phone in record.phones) if record.phones else "No phones"
                row.append(phones)
            elif field == "Email":
                email = record.email.value if record.email else "No email"
                row.append(email)
            elif field == "Birthday":
                birthday = record.birthday if record.birthday else "No birthday"
                row.append(birthday)
            elif field == "Address":
                address = str(record.address) if record.address else "No address"
                row.append(address)
            else:
                row.append("N/A")

        table.add_row(row)
    return str(table)
        