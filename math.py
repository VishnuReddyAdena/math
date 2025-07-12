import math
number = int(input("Enter a  number:"))

if number > 0:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    print("square root:",square_root)
    print("Logarithm:",natural_log)
    print("sine:",sine_value)
else:
    print("Enter a valid number for squares and roots of anumber")
    