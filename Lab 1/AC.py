# Develop a Simple Average Calculator (This is Hardcode)

import sys  # provide access to command-line arugments and various system


def calculate_average(a, b, c):  # defines a function calculate_average
    try:  # try and except wait for an error to occur and handles it afterward
        a = float(a)
        b = float(b)
        c = float(c)
        average = (a + b + c) / 3
        # return to calculate_average and rounded to two decimal places
        return round(average, 2)
    except ValueError:  # defines as exception handler
        return None


if len(sys.argv) != 4:  # check whether the length of the sys.argv list is not equal to 4 , one element + 3 variable
    print("Your input is invalid!")
else:
    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    result = calculate_average(a, b, c)
    if result is not None:
        print("Average: {:.2f}".format(result))
    else:
        print("Your input is invalid!")
""