# Develop a Simple Average Calculator

import sys

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    average = ((a + b + c)/3)
    average_rounded = round(average, 2)
    print("Average:"+format(average_rounded, ".2f"))

except ValueError:
    print("Your input is invalid!")