"""
# Part A - Phone Number Parser
We want to make a program (a function) in Python, which takes in a phone number 
as a string, checks if it is acceptable, and returns either `None` if not 
accepted, or the phone number as a tuple of strings as shown below.
"""

# parse_phone_number is the function that checks if the number value is a valid number, and makes it ready to be put into the tuple
def parse_phone_number(number):
    # The array splits off the + and tells it to start counting form the second place in the string, but was a bit cumbersome
    #array = number.split('+')[1]

    # spaces removes the spaces by replacing them with nothing
    spaces = number.replace(" ", "")
    # oN (only number) replaces the + with nothing, and steals the job from the array
    oN = spaces.replace("+", "")

    # if the length of oN is 10...
    if len(oN) == 10:
        #... go through oN  separate_numbers into a list ()
        #... make a list(the data type for an array) called separete_nubers and make each number its own item in the list
        separate_numbers = list(oN)

        # lCode(land code) is an empty array where the land code bit of a phone number will later be stored
        lCode = []
        # pNumber(phone number) is an empty array where the phone number will later be stored
        pNumber = []

        # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 by default, and ends at a specified number
        # for every i(integer) in len(oN), loop through and count them using range
        for i in range(len(oN)):
            
            # print(i) (was used to see how many numbers were in the range, counting from 0)

            # if the number i is before the first two spaces (counting from 0, so 0 and 1 (4 and 7))...
            if i < 2:
                #... put them into lCode, and...
                lCode.append(separate_numbers[i])
                #... join them together into one item with nothing separating them using "" (aka. '47'), stored in flCode(full land code)
                flCode = "".join(lCode)
            #... else if they're not in the first two spaces, ... 
            else:
                #... put them into pNumber, and...
                pNumber.append(separate_numbers[i])
                #... join them together into one item with nothing sparating them using "" (aka. everything after 47), stored in fpNumber(full phone number)
                fpNumber = "".join(pNumber)
       
        # The return keyword is to exit a function and return a value 
        # Return with what got stored in flCode and fpNumber
        return (flCode, fpNumber) # (code, number) or None
    #... else it isn't 10 spaces...
    else:
        #... print this message
        print("Not a valid phone number")

# parsed_number is the value where the now parsed phone number gets stored in after putting the number through the function parse_phone_number
parsed_number = parse_phone_number('+47 123 45 678')
# by printing parsed_number, you create the tuple it's supposed to be displayed as
print(parsed_number)  # ('47', '12345678') This is the tuple the number get put into