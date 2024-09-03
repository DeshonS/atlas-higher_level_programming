#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
else:
    last = number % -10
print(f"Last digit of {number} is {last}", end=" ")
if number > 5:
    print("and is greater than 5")
elif number < 6 & number != 0:
    print("and is less than 6 but not 0")
else:
    print("and is 0")
