"""
print ("hello")
print (3+4)
"""

with open('username.csv') as file:
    text = file.read()


lines = text.split('\n')
for line in lines:
    thing = line.split(';')
    for item in thing:
        print(f'{item:13}', end='')
    print('\n')