"""
CP1404 example - checking valid numbers
"""
__author__ = 'Jason Holdsworth'


def get_valid_number(lower, upper, prompt="Enter number: "):
    valid = False
    number = 0
    while not valid:
        try:
            number = int(input(prompt))
            if number < lower or number > upper:
                print("Number is out of range")
            else:
                valid = True
        except ValueError:
            print("Number is bad")
    return number


# testing examples - comment out to run

# age = get_valid_number(0, 120, "How old are you? ")
# print("You are", age, "years old")
# print("Finished")
#
# number_of_kids = get_valid_number(0, 30, "How many kids? ")
# print(number_of_kids)

# number = get_valid_number(0, 30)
# print(number)