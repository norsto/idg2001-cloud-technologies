def get_location(path):
    path = path.replace('\\', '/')
    list_of_elements = path.split('/')
    # print(list_of_elements)
    new_elements = list_of_elements[:-1]  # from start, to end-1
    # print(new_elements)
    new_path = '/'.join(new_elements)
    return new_path

result = get_location('google.com/folder/file.pdf')  # -> 'google.com/folder/'
print(result)


def get_new_path(old_path, old, new):
    # v1
    # new_path = old_path.replace(old, new)  # Almost works
    new_path = old_path.replace(f'/{old}/', f'/{new}/')  # Actually works

    # v2
    elements = old_path.split('/')
    for i in range(len(elements)):
        if elements[i] == old:
            elements[i] = new
    new_path = '/'.join(elements)

    return new_path


get_new_path('google.com/folder1/folder2/file.pdf',
            'folder1', 'another_folder')
            # -> 'google.com/another_folder/folder2/file.pdf'
