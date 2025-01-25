# Part A - Phone Number Parser
We want to make a program (a function) in Python, which takes inn a phone number as a string, checks if it is acceptable, and returns either `None` if not accepted, or the phone number as a tuple of strings as shown below.

```python
def parse_phone_number(number):
    ...
    return ...  # (code, number) or None


parsed_number = parse_phone_number('+47 123 45 678')
print(parsed_number)  # ('47', '12345678')
```

Here, the tuple should consist of (1) the country code (use '47' if none is given), and (2) the ctual phone number, as a number, no spaces or other dividing symbols.

Assume:
- the country code always starts with a pluss ('+'). If no pluss is given, the phone number has no country code. (Use '47'.)
- the country code is always either separated from the rest of the phone number with either a space (' ') or a dash ('-').

An invalid number is a string which contains values other than the plus ('+'), integers, spaces and dashes ('-').


# Part B - Phone Number Prettifyer
A function which takes a phone number in the format shown above, and returns in the following format, based on the following country codes.

| Country code | Format example |
|-|-|
| 1 | '+1 123 456 7890' |
| 41 | +41 12 345 67 89' |
| 47 | '+47 123 45 678' |

Assume all numbers will be this long.

## Additional feature
Assuming the separator is always spaces: See if you can make it easy to add more formats in the code. E.g., by using some form of dictionary/JSON, and a list of the number of integers per block.


# Solution
See the `solution.py` file for a suggested solution, as well as tests. Other solutions are also valid, of course.
