#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    str = f"Last digit of {number} is {number % 10} and is greater than 5"
elif number < 6 & number != 0:
    str = f"Last digit of {number} is {number % 10} and is less than 6 and not 0"
else:
    str = f"Last digit of {number} is {number % 10} and is 0"
print(str)
