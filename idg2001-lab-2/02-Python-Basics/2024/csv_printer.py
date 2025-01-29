# Load text
with open('2-Python/contacts.csv') as f:
    text = f.read()


# Split text into list of lines
lines = text.split('\n')

# for each line
for line in lines:
    # Alternative solution?
    # new_line = line.replace(';', '     ')

    # Split line into individual items
    items = line.split(';')

    # For each line
    for item in items:
        # Print item (13 col width)
        print(f'{item:13}', end='')

    # Add new-line before next line
    print()
