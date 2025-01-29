def consists_of(string, valid_characters):
    '''Help function.'''
    for char in string:
        if char not in valid_characters:
            return False
    return True


def is_valid(email):
    '''Solving using negative tests.
    Probably better to just use regex tbh'''

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '-_.+'

    if email.count('@') != 1:
        return False

    before, after = email.split('@')

    # before
    if not consists_of(before, letters + numbers + symbols):
        return False

    # after
    if '.' not in after:
        return False

    if not consists_of(after, letters + '.'):
        return False

    for substring in after.split('.'):
        if len(substring) < 1:
            return False

    return True


print(is_valid('paul.knutson@ntnu.no'))  # True
print(is_valid('paul.knutson@ntnu.co.uk'))  # True
print(is_valid('paul.knutson@.co.uk'))  # False
print(is_valid('paul knutson@ntnu.no'))  # False
