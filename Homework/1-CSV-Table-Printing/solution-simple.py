# Load file
with open('Homework/1-CSV-Table-Printing/example.csv') as file:
    data = file.read()


# Split the data, and separate the header from the values
lines = data.split('\n')
header = lines[0]  # First line
values = lines[1:]  # All the other lines

# Hardcode line
sep_line = '+' + '-'*15 + '+' + '-'*15 + '+' + '-'*15 + '+' + '-'*15 + '+\n'


# Building the table string (instead of printing it part by part)
text = ''

# Separator line 1
text += sep_line

# Header
for item in header.split(','):
    # Using built-in functions:
    # item_text = f'| {item.ljust(15)} '

    # Manually calculating the remaining spaces
    item_length = len(item)
    remaining_spaces = 15 - item_length - 2  # 2 because of the pipe and space
    item_text = f'| {item} ' + ' '*remaining_spaces

    text += item_text

# Add final pipe and newline
text += '|\n'

# Separator line 2
text += sep_line

# Values (copy/paste from header section, but for each line)
for line in values:
    for item in line.split(','):
        item_length = len(item)
        remaining_spaces = 15 - item_length - 2
        item_text = f'| {item} ' + ' '*remaining_spaces

        text += item_text

    text += '|\n'

# Separator line 3
text += sep_line

# Print the table
print(text)
