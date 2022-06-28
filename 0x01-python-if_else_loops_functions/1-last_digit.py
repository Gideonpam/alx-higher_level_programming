#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

# 1. Get the string representation
num_str = repr(number)
# 2. Access the last string of the digit string:
last_digit_str = num_str[-1]
# 3. Convert the last digit string to an integer:
last_digit = int(last_digit_str)
message = "Last digit of "
# if last_digit > 5:
#     if number > 0:
#         print(f"{message} {number} is {last_digit_str} "
#         "and is greater than 5")
#     else:
#         print(f"{message} {number} is -{last_digit_str} "
#         "and is less than 6 and not 0")
# elif last_digit == 0:
#     print(f"{message} {number} is {last_digit_str} and is 0")
# elif last_digit < 6 and last_digit != 0:
#     if number > 0:
#         print(f"{message} {number} is {last_digit_str} "
#         "and is less than 6 and not 0")
#     else:
#         print(f"{message} {number} is -{last_digit_str} "
#         "and is less than 6 and not 0")

if number < 0:
    last_digit = -last_digit
print("{}{} is {} and is ".format(message, number, last_digit), end="")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")

