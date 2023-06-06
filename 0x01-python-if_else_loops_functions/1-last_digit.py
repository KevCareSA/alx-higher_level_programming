#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    left_over = number % -10
else:
    left_over = number % 10

if left_over > 5:
    print(
        f"Last digit of {number:d} is {left_over} and is greater than 5"
        )
elif left_over < 6 and left_over != 0:
    print(
        f"Last digit of {number:d} is {left_over} and is less than 6 and not 0"
        )
elif left_over == 0:
    print(f"Last digit of {number:d} is {left_over} and is 0")
