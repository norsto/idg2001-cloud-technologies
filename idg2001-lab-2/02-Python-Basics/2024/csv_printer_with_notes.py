"""
We have a csv-structure, and want something like the following:

Username    Ident..
booker12    9012
johnson..   4081

I.e., we want th columns to be aligned. The width isn't super imporant, but
they should be aligned.

We are given the how-to-read-file part of the code.
"""


with open('2-Python/contacts.csv') as f:
    text = f.read()


"""
Ideas:
- Replace ";" with a lot of spaces.
- Split into lines and items, and print those out individually.

We have the following functions to replace and split in strings
"""


example_string = 'abd;def'
example_string = example_string.replace(';', ' ')  # Replace ; with space.
example_string = example_string.split()  # Split on any whitespace.


"""
If we split into a list of lines, and replace ";" with multiple spaces (or a
tab or two), we would get a somewhat working result.
"""


lines = text.split('\n')  # Split into lines.
for line in lines:
    new_line = line.replace(';', '\t\t')  # Replace ; with two tabs.
    print(new_line)


"""
This works, but it's not very pretty. We can do better. We need to fix an
exact width for each column, and then print each item with that width. We can
use the f-string syntax for this.

f'{item:20}'  # Print item with width 20.

Let's do this with all items in all
columns. Importantly, we need to add a newline/line break each time we're done
with a line. An empty print should do this.

Impotant note about the print function:

print()               # Print empty line.
print('hey')          # Print 'hey' _and a newline_.
print('hey', end='')  # Print 'hey' _without_ a newline.
"""


lines = text.split('\n')  # Split into lines.
for line in lines:
    items = line.split(';')  # Split into items.
    for item in items:
        print(f'{item:20}', end='')  # Print item with width 20.
    print()  # Add newline before next line.


"""
This works great! We can see that the width is a bit too much, but we can just
try to change it to 15 or 10 or something. For my CSV-file, 13 works well.
"""


lines = text.split('\n')  # Split text into lines.
for line in lines:
    items = line.split(';')  # Split one-and-one line into items.
    for item in items:
        print(f'{item:13}', end='')  # Print item with width 13.
    print()  # Add newline before next line.
