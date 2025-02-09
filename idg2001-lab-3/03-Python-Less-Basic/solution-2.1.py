# Read text from file.
with open('04-Python-Less-Basic/sample-1.vcf') as f:
    text = f.read()

# Split text by line.
lines = text.split('\n')

# Create empty dictionary/JSON.
contact = {}

# Loop through lines.
for line in lines:
    # If line has no colon, skip this line.
    if ':' not in line:
        continue

    # Split line on colon, and add to dictionary.
    key, value = line.split(':')
    contact[key] = value

# Write out (but pretty).
import json
print(json.dumps(contact, indent=4))
