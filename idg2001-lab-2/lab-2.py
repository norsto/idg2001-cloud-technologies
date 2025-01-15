#path/URI parser
#given path URL/URI, i.e., /Users/Documents/IDG2001/Lab/Python/README.md or 
#/Users/Documents/IDG2001/Lab/Python/README.md, we want the following two functonalities (functions?).


#1. Get the location of the file, without the file at the end

#ex.1: urlpars urllib.parse:
#components of the URL https://www.example.com/path/to/file?query=value are:
#   Scheme: https
#   Netloc: www.example.com
#   Path: /path/to/file
#   Query: query=value
#This function is especially useful when you need to analyze or manipulate URLs


#os is more for the local
# the os module in Python provides functions for interacting with the operatong system
import os
# it's used for checking if a path exists, creating, removing or renaming files and directories, and manipulating file paths

#urllib is more for URLs
#The urllib.parse module is part of Python's standard library designed for parsing and handeling URL's
#urlparse is a spesific function within urllib.pars that breaks a URL into its components, ex.1
from urllib.parse import urlparse 

#def is function
def get_location(path):
    
    #if theres a :// in the path, handle/parse it like an URL
    if "::/" in path:
        #put it through the urlparse
        #urlparse breaks the URL into components, ex.1
        parsed = urlparse(path)
        #os.path.dirname extracts the directory-like part of the path in the URL
        #parsed.path is the resource path from the url
        location = os.path.dirname(parsed.path)

        #rebuild the location with the scheme and host if present
        return parsed.scheme + "://" + parsed.netloc + location if parsed.netloc else location
    else: #Treat it as a local file path
        #os.path.dirname extracts the directory path without the file
        return os.path.dirname(path)

#a string representing a file's path on a local filesystem
local_path = "/Users/Documents/IDG2001/Lab/Python/README.md"
#a string representing a file's location on the web
url = "https://www.example.com/drive/folder1/folder2/file1.pdf"

#The function get_location is called twise, once with the local path and once with the UTL, to extract the "location" (the directory or path containing the file)
#get_location(local_path) is invoked with the argument "/Users/Documents/IDG2001/Lab/Python/README.md"
print("Location, Local path:", get_location(local_path))
#get_location(url) is invoked with the argument "https://www.example.com/drive/folder1/folder2/file1.pdf"
#it get's recognized as an url due to the :// bit
print("Location, URL:", get_location(url))


# 2. replace folder... fail

def get_location(path):
    #splits the given path into a list of elements using / as the delimiter
    list_of_elements = path.split('/')
    #output: list_of_elements = ["https:", ""; "www.example.com", "drive", "folder1", "folder2", "file1.pdf"]
    print(list_of_elements)
    #list_of_elements[:1] takes only the first element of the list ["https:"] and ignores the rest
    new_elements = list_of_elements[:1]
    #output: new_elements = ["https:"]
    print(new_elements)
    #output new_path: "https:"
    new_path = '/'.join(new_elements)
    return new_path

result = get_location("https://www.example.com/drive/folder1/folder2/file1.pdf")
print(result)

#the folder thing u can add ...IDG2001/2025/...


# 2. Replace a folder with another folder, e.g., replacing "folder1" with "folder2". This should not affect "folder12".

#def defines a function. Functoions are a reusable block of code designed to perform a spesific task
#get_location is the name of the function and is used to call the function elswhere in the code
#path is the parameter of the functon. A parameter acts as a placeholder for a value (an argument) that will be passed
    #to the function when it is called. In this case, path is expected to be a string (like a file path or a URL)
def get_location(path):
    #splits the input string into a list of path elements
    list_of_elements = path.split('/')
    #print(list_of_elements)
    
    #list comprehension
    new_elements = [
        #checks each element in the list. If the element is "folder1" with "folder2". otherwise it keeps the element unchanged
        'folder2' if element == 'folder1' else element for element in list_of_elements
    ]

    #Joins the list back into a single string using / as the seperator, aka. putting the / back where it was
    new_path = '/'.join(new_elements)
    #the result of the function's processing is returned using the return statement
    return new_path

#calls the get_location function and run through the given URL/string and stores the value in result
result = get_location("https://www.example.com/drive/folder1/folder2/file1.pdf")
#calls rhe get_location function with the given URL/string as an argument
#The function processes the string and returns a value, which is stored in the variable result
print(result)