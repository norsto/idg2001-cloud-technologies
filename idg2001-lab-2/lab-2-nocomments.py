#1. Get the location of the file, without the file at the end

import os
from urllib.parse import urlparse 

def get_location(path):
    
    if "::/" in path:
        parsed = urlparse(path)
        location = os.path.dirname(parsed.path)

        return parsed.scheme + "://" + parsed.netloc + location if parsed.netloc else location
    else:
        return os.path.dirname(path)

local_path = "/Users/Documents/IDG2001/Lab/Python/README.md"
url = "https://www.example.com/drive/folder1/folder2/file1.pdf"

print("Location, Local path:", get_location(local_path))
print("Location, URL:", get_location(url))


# 2. Replace a folder with another folder, e.g., replacing "folder1" with "folder2". This should not affect "folder12".

def get_location(path):
    list_of_elements = path.split('/')
    
    new_elements = [
        'folder2' if element == 'folder1' else element for element in list_of_elements
    ]

    new_path = '/'.join(new_elements)
    return new_path

result = get_location("https://www.example.com/drive/folder1/folder2/file1.pdf")
print(result)