# Bonus
stack_size_lookup = {
    'Stone': 64,
    'Dirt': 64,
    'Egg': 16
}


class Stack:
    def __init__(self, block_type, amount):
        self.block_type = block_type
        self.amount = amount

        # Bonus
        self.stack_size = 64
        if self.block_type in stack_size_lookup:
            self.stack_size = stack_size_lookup[self.block_type]

    def add(self, other_stack):
        # Illegal add
        if self.block_type != other_stack.block_type:
            return None

        # Add other -> self up to 64* (yay maths!)
        self.amount += other_stack.amount
        other_stack.amount = 0

        if self.amount > self.stack_size:  # Bonus. Without: 64
            other_stack.amount = self.amount - self.stack_size
            self.amount = self.stack_size

    def __str__(self):
        return f'{self.amount}'

    # Even more features :D
    def __iadd__(self, other):
        self.add(other)
        return self


s1 = Stack('Stone', 40)
s2 = Stack('Stone', 30)
s3 = Stack('Dirt', 20)

print(s1)  # 40
print(s2)  # 30
print(s3)  # 20
print()

s2.add(s1)  # Top up s2 with s1
# s2 += s1  # Does the same thing as s1.add(s1)

print(s1)  # 6
print(s2)  # 64
print(s3)  # 20
print()

s3.add(s2)  # Illegal add, no effect

print(s1)  # 6
print(s2)  # 64
print(s3)  # 20
print()
