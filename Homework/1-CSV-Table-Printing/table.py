with open('Homework/1-CSV-Table-Printing/example.csv') as file:
    text = file.read()

lines = text.split()

for line in lines:
    element = line.split(',')

    for item in element:
        print(f'{item:12}', end='')

    print('\n')