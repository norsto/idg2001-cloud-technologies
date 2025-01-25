#####################
## parse_phone_number
#####################

def parse_phone_number(number):
    # Check if valid.
    for char in number:
        if char not in '+- 0123456789':
            return None

    # Replace dash with space.
    number = number.replace('-', ' ')

    # Find country code.
    country_code = '47'  # Default
    cc_width = 0
    if number[0] == '+':  # Override
        country_code = number.split(' ')[0]
        cc_width = len(country_code)

    # Remove country code from number.
    number = number[cc_width:]

    # Remove spaces and +.
    number = number.replace(' ', '')
    country_code = country_code.replace(' ', '')
    country_code = country_code.replace('+', '')

    number_tuple = (country_code, number)
    return number_tuple


parsed_number = parse_phone_number('+47 123 45 678')
print(parsed_number)  # ('47', '12345678')


# Tests
assert parse_phone_number('+47 123 45 678') == ('47', '12345678'), \
    parse_phone_number('+47 123 45 678')

assert parse_phone_number('123-45-678') == ('47', '12345678'), \
    parse_phone_number('123-45-678')

assert parse_phone_number('123 45 678') == ('47', '12345678'), \
    parse_phone_number('123 45 678')

assert parse_phone_number('12345678') == ('47', '12345678'), \
    parse_phone_number('12345678')

assert parse_phone_number('+A12-B34-C56') == None, \
    parse_phone_number('+A12-B34-C56')


##########################
## phone_number_prettifyer
##########################

def phone_number_prettifyer(number_tuple):
    country_code, number = number_tuple

    # Country code formating.
    if country_code == '1':
        number = f'+1 {number[:3]} {number[3:6]} {number[6:]}'
    elif country_code == '41':
        number = f'+41 {number[:2]} {number[2:5]} {number[5:7]} {number[7:]}'
    elif country_code == '47':
        number = f'+47 {number[:3]} {number[3:5]} {number[5:]}'
    else:
        number = f'+{country_code} {number}'

    return number


formatted_number = phone_number_prettifyer(('47', '12345678'))
print(formatted_number)  # +47 123 45 678


# Tests
assert phone_number_prettifyer(('1', '1234567890')) == '+1 123 456 7890', \
    phone_number_prettifyer(('1', '1234567890'))

assert phone_number_prettifyer(('41', '123456789')) == '+41 12 345 67 89', \
    phone_number_prettifyer(('41', '123456789'))

assert phone_number_prettifyer(('47', '12345678')) == '+47 123 45 678', \
    phone_number_prettifyer(('47', '12345678'))
