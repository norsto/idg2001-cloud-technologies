def resolve(path: str) -> str:
    '''/path/to/folder1/../file.txt -> /path/to/file.txt'''
    liste = path.split('/')

    index = 0
    while index < len(liste):
        if liste[index] == '..':
            del liste[index]
            del liste[index - 1]
            index -= 1
        else:
            index += 1

    new_path = '/'.join(liste)
    return new_path


# Test setup
in_data = '/path/to/folder1/../folder/../file.txt'
result = resolve(in_data)
expected = '/path/to/file.txt'

# Run test
assert result == expected, \
    f'resolve("{in_data}") =/= expected:\n{result}\n{expected}'
