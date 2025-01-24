# parsing a csv file
"""
print ("hello")
print (3+4)
"""

# the with statement ensures the file is closed automatically after reading
# open() as file opens the file and assigns it to the variable file
with open('idg2001-lab-1/username.csv') as file:
    # the file gets read and saved into the variable text
    text = file.read()

# .split splits the text on the end of a line/ at new line and saves the lines in the variable lines
lines = text.split('\n')
# a loop goes through each line of the file, where line represents each line/row as a string
for line in lines:
    # line.split splits the lines at ;, and thing becomes a list of those values
    thing = line.split(';')
#    print(thing)
    # item prints out only the item bit in thing, not the array brackets and ''
    for item in thing:
        # f is a formatted string and it lets you include the value of python expressions
        # each item is 13 characters, no matter its original length
        # end = '' prevents printing a new line after each item, keeping them on the same row
        print(f'{item:13}', end='')
    # prints each line on it's own row
    print('\n')