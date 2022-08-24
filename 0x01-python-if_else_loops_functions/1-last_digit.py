#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = abs(number) % 10
if new_number > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,new_number), end="")
elif new_number == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
