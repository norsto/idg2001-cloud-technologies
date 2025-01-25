# Idempotence
> Difficulty: Easy

The term idempotence (in computer science, not mathematics) means roughly that a function call, API call, etc. can be called multiple times without giving a different result than calling it once.

Appending an item to the end of a list is a non-idempotent action.
```python
list = [1, 2, 3]
list.append(4)  # [1, 2, 3, 4]
list.append(4)  # [1, 2, 3, 4, 4]
```

Setting the first value equal to 5 is an idempotent action.
```python
list = [1, 2, 3]
list[0] = 5  # [5, 2, 3]
list[0] = 5  # [5, 2, 3]
```

This is relevant when there is a possibility that the call will happen multiple times by accident, or for other reasons.


## Problem 1
Make a function (`secure_append(list, value)`) which is idempotent. That is, running once vs. running multiple times will result in the same result.

I want to be able to run something like the following.
```python
list = [1, 2, 3]
list = secure_append(list, 4)  # |1, 2, 3, 4]
list = secure_append(list, 4)  # |1, 2, 3, 4]
list = secure_append(list, 5)  # |1, 2, 3, 4, 5]
```

So the second append will not add anything, because the value `4` is already added.


## Problem 2
Same as problem 1, but now use the following structure instead of the simple list.
```python
db = [
    {'id': 1, 'message': 'hello'},
    {'id': 2, 'message': 'hi'},
    {'id': 3, 'message': 'howdy'}
]
```

And appending should not happen when the ID already exists.

Expected behvaviour:
```python
db = [...]  # Same 3 dicts as above
db = secure_append(db, {'id': 4, 'message': 'something'})  # Added: new item/id
db = secure_append(db, {'id': 4, 'message': 'something'})  # Not added: existing id
db = secure_append(db, {'id': 4, 'message': 'something else'})  # Not added: existing id
db = secure_append(db, 'id': 5, 'message': 'something'})  # Added: new item/id

print(db)
```

Output (but I wrote it pretty here):
```
db = [
    {'id': 1, 'message': 'hello'},
    {'id': 2, 'message': 'hi'},
    {'id': 3, 'message': 'howdy'},
    {'id': 4, 'message': 'something'},
    {'id': 5, 'message': 'something'}
]
```

### Bonus
What if we want the system to update id:4 when the message is a new one? What would we have to change?
