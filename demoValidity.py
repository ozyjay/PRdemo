"""
CP1404 example - checking valid numbers
"""
__author__ = 'Jason Holdsworth'


def get_valid_number(lower, upper, prompt="Enter number: "):
    valid = False
    x = 0
    while not valid:
        try:
            x = int(input(prompt))
            if x < lower or x > upper:
                print("Number is out of range")
            else:
                valid = True
        except ValueError:
            print("Number is bad")
    return x


# test
# age = get_valid_number(0, 120, "How old are you? ")
# print("You are", age, "years old")
# print("Finished")
#
# number_of_kids = get_valid_number(0, 30, "How many kids? ")
# print(number_of_kids)

# number = get_valid_number(0, 30)
# print(number)