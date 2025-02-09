# Read text from file.
with open('04-Python-Less-Basic/sample.vcf') as f:
    text = f.read()

# Split text by line.
lines = text.split('\n')

# Create empty list and dictionary/JSON.
contacts = []
contact = {}

# Loop through lines.
for line in lines:
    # If line has no colon, skip this line.
    if ':' not in line:
        continue

    # Split line on colon, and add to dictionary.
    key, value = line.split(':')
    contact[key] = value

    # When encountering a new contact
    if key == 'END':
        # If key is END, add contact to list and create new contact.
        contacts.append(contact)
        contact = {}

# If contact (has value), add final contact.
if contact:
    contacts.append(contact)


# Skrive ut (pent).
import json
print(json.dumps(contacts, indent=4))
