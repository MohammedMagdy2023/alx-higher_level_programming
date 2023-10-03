#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
print(f"Last digit of {number:d} is {ld}", end =" ")
if number % 10 > 5:
    print("and is greater than 5")
elif number % 10 < 6 and number % 10 != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")

