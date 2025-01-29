# Problems
Try solving them before looking at the solutions. And remember, there are many ways to solve each of the problems. With and without importing modules.


## Problem 1: Path/URI parsing
Given a path or URI/URL, i.e., `www.google.com/drive/folder1/folder2/file1.pdf` or `/Users/Documents/IDG2001/2025/Lab/Python/README.md`, we want the following two functionalities (functions?).

1. Get the location of the file, without the file at the end
2. Replace a folder with another folder, e.g., replacing "folder1" with "folder2". This should not affect "folder12".


## Problem 2: Email checker
Make the function `is_valid` which
takes in an email (string) and returns
a bool saying whether or not it is a
valid email address. It should be
valid if the following is true.

- Has one @
- Has letters and/or numbers before @
- Has letters and/or numbers after @
- Has a dot (.) after @ e.g., ntnu.no


## Problem 3: Minecraft stack
Finish the class such that
the rest of the code works as
illustrated in the comments
below.

```python
class Stack:
    ...

s1 = Stack('Stone', 40)
s2 = Stack('Stone', 30)
s3 = Stack('Dirt', 20)

print(s1)  # 40
print(s2)  # 30
print(s3)  # 20

s2.add(s1)  # Top up s2 with s1

print(s1)  # 6
print(s2)  # 64
print(s3)  # 20

s3.add(s2)  # Illegal add, no effect

print(s1)  # 6
print(s2)  # 64
print(s3)  # 20
```

### Bonus
Make it support different stack sizes for different types (stone: 64, dirt: 64, egg: 16, etc.)
