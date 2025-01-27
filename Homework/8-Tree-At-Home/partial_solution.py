import os
import sys


# `python script.py arg1 arg2`
arguments = sys.argv
print(arguments)  # [script.py, arg1, arg2]

# Similar to the command `ls`.
os.listdir()  # Lists content of CWD/PWD
os.listdir("FolderName")  # Lists content of folder called FolderName

for element in os.listdir():
    if element is folder:
        subdirs = os.listdir(folder)
