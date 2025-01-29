'''Problem: Minecraft stack
Finish the class such that
the rest of the code works as
illustrated in the comments
below.
'''

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
